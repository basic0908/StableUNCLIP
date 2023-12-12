clear
close all

defaultpath=pwd;
addpath(genpath([defaultpath '\functions']))
outputpath=[defaultpath '\data\RealtimeGeneration'];mkdir(outputpath)
vflist=dir([defaultpath '\data\RSM\*.mat']);
[indx,tf] = listdlg('ListString',{vflist.name},'PromptString','select a file', 'SelectionMode','single');
load([defaultpath '\data\RSM' '\' vflist(indx).name])

%%VIE EEG
vflist=dir([defaultpath '\VIErecordingFolder']);vflist={vflist(3:end).name};
[indx,tf] = listdlg('ListString',vflist,'PromptString','脳波を収録しているPCフォルダを選択してください', 'SelectionMode','single');
selpath=[defaultpath '\VIErecordingFolder\' vflist{indx}];
filelist=dir([selpath '\VieOutput\VieRawData_*.csv']);
for i=1:length(filelist);delete([filelist(i).folder '\' filelist(i).name]);end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% EXperiment Setup
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
savefilename=[defaultpath '\data\RealtimeGeneration\' subName  '-' TargetCat '-' datestr(now,30)   ];

AssertOpenGL;
%% Keyboardのチェック
KbName('UnifyKeyNames');  % OSで共通のキー配置にする
DisableKeysForKbCheck([]);% 無効にするキーの初期化
[ keyIsDown, secs, keyCode ] = KbCheck;% 常に押されるキー情報を取得する
keys=find(keyCode) ;%
DisableKeysForKbCheck(keys);

% %% Variables
Screen('Preference', 'SkipSyncTests', 1);%　これを入れないと時々エラーが出る
Screen('Preference', 'TextRenderer', 1);
Screen('Preference', 'TextAntiAliasing', 0);
Screen('Preference', 'TextAlphaBlending', 0);
windowsize=[];
screenid = max(Screen('Screens'));
ScreenDevices = java.awt.GraphicsEnvironment.getLocalGraphicsEnvironment().getScreenDevices();
MainScreen = java.awt.GraphicsEnvironment.getLocalGraphicsEnvironment().getDefaultScreenDevice().getScreen()+1;
MainBounds = ScreenDevices(MainScreen).getDefaultConfiguration().getBounds();
MonitorPositions = zeros(numel(ScreenDevices),4);
for n = 1:numel(ScreenDevices)
    Bounds = ScreenDevices(n).getDefaultConfiguration().getBounds();
    MonitorPositions(n,:) = [Bounds.getLocation().getX() + 1,-Bounds.getLocation().getY() + 1 - Bounds.getHeight() + MainBounds.getHeight(),Bounds.getWidth(),Bounds.getHeight()];
end

% [w, rect] = Screen('OpenWindow', screenid, 128, [10 30 60 30]); %test用
% % [w, rect] = Screen('OpenWindow',screenid, 128 , [MonitorPositions(1,1)  MonitorPositions(1,2) MonitorPositions(1,1)+MonitorPositions(1,3) MonitorPositions(1,4)-250]); %test
% 
% Screen('TextFont',w, 'MS Mincho');
% Screen('TextSize',w, 25);
% Screen('TextStyle', w, 0);
% Screen('BlendFunction', w, 'GL_SRC_ALPHA', 'GL_ONE_MINUS_SRC_ALPHA');
% Screen('TextFont', w, '-:lang=ja');

windowsize=get(0,'MonitorPositions');
h=figure('Position',[windowsize(1,1) windowsize(1,2) windowsize(1,3) 230],'Color','k');%alwaysontop(h)
h.MenuBar='none';h.ToolBar='none';
% [centerX, centerY] = RectCenter(rect);%画面の中央の座標
% HideCursor();
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% EEG SETTING (VIE ZONE)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
filename=[selpath '\VieOutput\' 'VieRawData.csv' ];%             filename=[filelist(1).folder '\' filelist(1).name ];%VieRawData.csv
opts = detectImportOptions(filename);
opts.SelectedVariableNames = [2 3];
SAMPLE_FREQ_VIE=600;
FreqWindow=[4:0.5:40];
timeWindow=4;

%% Filter Setting
[B1f,A1f] = butter(4,[3/(SAMPLE_FREQ_VIE/2) 40/(SAMPLE_FREQ_VIE/2)]);% 3~40Hzバタワースフィルタ設計
Zf1=[];


%% EEG Monitor Window
mtimeWindow=4;
cplotdata=repmat(0,SAMPLE_FREQ_VIE*mtimeWindow,3)+[40 0 -40];
cidx=1;
cbaseline=[0 0 0];

% % Signal Quality Parameter
NoiseMetricsLabel={'Average Power_L' 'Average Power_R' 'RMS_L' 'RMS_R' 'MaxGradient_L' 'MaxGradient_R' 'ZeroCrossing Rate_L' 'ZeroCrossing Rate_R' 'Kurtosis_L' 'Kurtosis_R'};
NoiseMU=[138.502300000000	138.502300000000	12.1827000000000	12.1827000000000	103.387000000000	103.387000000000	0.0353000000000000	0.0353000000000000	10.1240000000000	10.1240000000000];
NoiseSigma=[123.240600000000	123.240600000000	6.02540000000000	6.02540000000000	69.4416000000000	69.4416000000000	0.00390000000000000	0.00390000000000000	2.89900000000000	2.89900000000000];

%Screen setting
ScreenDevices = java.awt.GraphicsEnvironment.getLocalGraphicsEnvironment().getScreenDevices();
MainScreen = java.awt.GraphicsEnvironment.getLocalGraphicsEnvironment().getDefaultScreenDevice().getScreen()+1;
MainBounds = ScreenDevices(MainScreen).getDefaultConfiguration().getBounds();
MonitorPositions = zeros(numel(ScreenDevices),4);
for n = 1:numel(ScreenDevices)
    Bounds = ScreenDevices(n).getDefaultConfiguration().getBounds();
    MonitorPositions(n,:) = [Bounds.getLocation().getX() + 1,-Bounds.getLocation().getY() + 1 - Bounds.getHeight() + MainBounds.getHeight(),Bounds.getWidth(),Bounds.getHeight()];
end

windowsize=get(0,'MonitorPositions');
h=figure('Position',[windowsize(1,1) windowsize(1,2) windowsize(1,3) 200],'Color','k');%alwaysontop(h)
h.MenuBar='none';h.ToolBar='none';

EEGplot=plot([1:SAMPLE_FREQ_VIE*mtimeWindow]/SAMPLE_FREQ_VIE,cplotdata-cbaseline,'LineWidth',1);
ha1 = gca;ha1.GridColor=[1 1 1];
set(gca,'Color','k')
h_yaxis = ha1.YAxis; % 両 Y 軸の NumericRulerオブジェクト(2x1)を取得
h_yaxis.Color = 'w'; % 軸の色を黒に変更
h_yaxis.Label.Color = [1 1 1]; %  軸ラベルの色変更
h_xaxis = ha1.XAxis; % 両 Y 軸の NumericRulerオブジェクト(2x1)を取得
h_xaxis.Color = 'w'; % 軸の色を黒に変更
h_xaxis.Label.Color = [1 1 1]; %  軸ラベルの色変更
set(gca,'Color','k')
xlim([0 4]);
titletext=title(['EEG (' num2str(round(0,2)) 's)'],'Color' ,'w', 'FontSize', 22);
xlabel('time (s)');
ylabel('uV');
yline(0,'w--');
ylim([-75 75]);
lgd=legend(EEGplot,{'L' 'R' 'diff'});
lgd.TextColor=[1 1 1];




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% START
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
EndFlag=0;
Data={};TrialNo=1;noiseFlag=[];NoiseMatsub=[];cNoise=[];g=1;PredictedcvecHist=[];TimeHist=[];
%% ready
% % DrawFormattedText(w,double(['SPACEキーを押してして計測スタート']), 'center', 'center',  WhiteIndex(w));
% Screen('Flip', w);%上で指定された情報を画面に表示
alldataV=[];
opts.DataLines=[2 inf];
craw=size(readmatrix(filename,opts).*18.3./64,1);% Read Start row

while 1
    WaitSecs(0.1)
    %% store EEG(VIE ZONE)
    opts.DataLines=[craw+1 inf];
    tempdataV=readmatrix(filename,opts).*18.3./64;
    if ~isempty(tempdataV)
        tempdataV=[tempdataV tempdataV(:,2)-tempdataV(:,1)];
        alldataV=[alldataV;tempdataV];
        craw=craw+size(tempdataV,1);

        [tempdata1,Zf1] = filter(B1f, A1f, tempdataV,Zf1); %Zf1:初期条件
        if cidx+size(tempdataV,1)-1<SAMPLE_FREQ_VIE*mtimeWindow
            cplotdata(cidx:cidx+size(tempdataV,1)-1,:)=tempdata1;
            cidx=cidx+size(tempdataV,1);
        else
            cplotdata(cidx:end,:)=tempdata1(end-(size(cplotdata,1)-cidx):end,:);
            cidx=1;
            cbaseline=nanmean(cplotdata);
        end
    end

    %% Noise Calc
    cNoiseMat=[];
    cdata=cplotdata(:,[1 2]);
    [pxx,f] = pwelch(cdata,SAMPLE_FREQ_VIE*timeWindow,0,FreqWindow,SAMPLE_FREQ_VIE);
    cNoiseMat([1 2])=sum(pxx);
    cNoiseMat([3 4])=rms(cdata);
    cNoiseMat([5 6])=max(gradient(cdata));
    %              zeroCross = cdata(1:end-1,:).*cdata(2:end,:) < 0;
    %              cNoiseMat([7 8])= sum(zeroCross)./size(cdata,1);
    cNoiseMat([9 10]) = kurtosis(cdata);
    cNoiseMatz=(cNoiseMat-NoiseMU)./NoiseSigma;
    cNoisez=[mean(abs(cNoiseMatz([1 3 5  9]))) mean(abs(cNoiseMatz([2 4 6  10])))];

    %% Display waveform
    set(titletext,'String',[ 'Press KEY to START  EEG ' 'sec NoiseLevel L=' num2str(cNoisez(1)) '  R=' num2str(cNoisez(2))] ,'Color','w');
    set(EEGplot(1),'YData',cplotdata(:,1)'+40); hold on% freqwidthに当たる部分を表示
    set(EEGplot(2),'YData',cplotdata(:,2)'); % freqwidthに当たる部分を表示
    set(EEGplot(3),'YData',cplotdata(:,3)'-40); % freqwidthに当たる部分を表示
    figure(h);

    [ keyIsDown, keyTime, keyCode ] = KbCheck;
    if keyIsDown
        if keyCode(KbName('ESCAPE'))
            EndFlag=1;
        end
        break
    end
end

opts.DataLines=[2 inf];
craw=size(readmatrix(filename,opts).*18.3./64,1);% Read Start row
%% Main Rec
%         alldataV=[];
tsstart=tic;
while 1 %toc(tsstart)<RecDuration+0.5
    %% EEG STORE
    opts.DataLines=[craw+1 inf];
    tempdataV=readmatrix(filename,opts).*18.3./64;
    if ~isempty(tempdataV) && size(tempdataV,1)>1
        tempdataV=[tempdataV tempdataV(:,2)-tempdataV(:,1)];
        alldataV=[alldataV;tempdataV];
        craw=craw+size(tempdataV,1);

        [tempdata1,Zf1] = filter(B1f, A1f, tempdataV,Zf1); %Zf1:初期条件
        if cidx+size(tempdataV,1)-1<SAMPLE_FREQ_VIE*mtimeWindow
            cplotdata(cidx:cidx+size(tempdataV,1)-1,:)=tempdata1;
            cidx=cidx+size(tempdataV,1);
        else
            cplotdata(cidx:end,:)=tempdata1(end-(size(cplotdata,1)-cidx):end,:);
            cidx=1;
        end
    end

    %% Noise Calc
    cNoiseMat=[];
    cdata=cplotdata(:,[1 2]);
    [pxx,f] = pwelch(cdata,SAMPLE_FREQ_VIE*timeWindow,0,FreqWindow,SAMPLE_FREQ_VIE);
    cNoiseMat([1 2])=sum(pxx);
    cNoiseMat([3 4])=rms(cdata);
    cNoiseMat([5 6])=max(gradient(cdata));
    cNoiseMat([9 10]) = kurtosis(cdata);
    cNoiseMatz=(cNoiseMat-NoiseMU)./NoiseSigma;
    cNoisez=[mean(abs(cNoiseMatz([1 3 5  9]))) mean(abs(cNoiseMatz([2 4 6  10])))];

    %% Display waveform
    set(titletext,'String',[ ' EEG (' num2str(round(toc(tsstart))) 's)    NoiseLevel L=' num2str(round(cNoisez(1),2)) '  R=' num2str(round(cNoisez(2),2))] ,'Color','w');
    set(EEGplot(1),'YData',cplotdata(:,1)'+40); hold on% freqwidthに当たる部分を表示
    set(EEGplot(2),'YData',cplotdata(:,2)'); % freqwidthに当たる部分を表示
    set(EEGplot(3),'YData',cplotdata(:,3)'-40); % freqwidthに当たる部分を表示
    drawnow;shg;

    [ keyIsDown, keyTime, keyCode ] = KbCheck;
    if keyIsDown
        if keyCode(KbName('ESCAPE'))
            EndFlag=1;
            break; % while 文を抜けます。
        end
    end

    %%
    if length(alldataV) > SAMPLE_FREQ_VIE*timeWindow
        cdata= alldataV(end-SAMPLE_FREQ_VIE*timeWindow+1:end,:);
        [pxx,f] = pwelch(cdata,SAMPLE_FREQ_VIE*timeWindow,0,FreqWindow,SAMPLE_FREQ_VIE);
        cpower=pxx(:,3);
        %% noise 処理
        [cdataf,Zf1]= filter(B1f, A1f,cdata,Zf1);
        [pxx,f] = pwelch(cdata(:,[1 2]),SAMPLE_FREQ_VIE*timeWindow,0,FreqWindow,SAMPLE_FREQ_VIE);
        NoiseMatsub(g,[1 2])=sum(pxx);
        NoiseMatsub(g,[3 4])=rms(cdataf(:,[1 2]));
        NoiseMatsub(g,[5 6])=max(gradient(cdataf(:,[1 2])));
        %             zeroCross = cdataf(1:end-1,[1 2]).*cdataf(2:end,[1 2]) < 0;
        %             NoiseMatsub(g,[7 8])=     sum(zeroCross)./size(cdataf(:,[1 2]),1);
        NoiseMatsub(g,[9 10]) = kurtosis(cdataf(:,[1 2]));
        cNoisez=(NoiseMatsub(g,:)-NoiseMU)./NoiseSigma;
        cNoise(g,:)=cNoisez;

        cNoisezMean=[mean(abs(cNoisez([1 3 5  9]))) mean(abs(cNoisez([2 4 6 10])))];
        if max(cNoisezMean)>ThuZ %%左右の電極の絶対振幅値の平均がTHを超えたら削除
            noiseFlag(g)=1;
            cpower=NaN;%1Trial 2windowNo 3freq 4channel
            Predictedcvec=repmat(NaN,1024,1);
        else
            noiseFlag(g)=0;
            %brain RSM
            [cRSM,p]=corr(MeanPower',cpower);
            crsmZ=(cRSM'-rsmMU)./rsmSIGMA;
            PredictedScore=[];
            X=crsmZ;
            for d=1:size(score1Z,2)
                PredictedScore(:,d)=nansum(X.* RSM2CLIPModel(d).CoefMat(1:end-1)',2)+    RSM2CLIPModel(d).CoefMat(end);
            end
            PredictedScore=(PredictedScore.*score1SIGMA)+score1MU;

            Predictedcvec=PredictedScore*coeff1'+mu1;
        end
        PredictedcvecHist(g,:)=Predictedcvec;
        writematrix(PredictedcvecHist,[outputpath '\'  'pred_emv_latest.csv'])
        TimeHist(g)=toc(tsstart);
        g=g+1;
        WaitSecs(1);
    end
end
save([savefilename 'Data.mat'], 'PredictedcvecHist','subName','selpath','noiseFlag','NoiseMatsub','cNoise','-v7.3');
% Screen('Flip', w);
WaitSecs(1)
sca
close all

