\NeedsTeXFormat{LaTeX2e}[1999/12/01]
\ProvidesClass{gdhsppt}[2011/03/31 2.0.1 The LaTeX class for the beamer]
%% import global options
\newif\iffonti\fontifalse % 使用xeCJK设置字体，
\DeclareOption{fonti}{\fontitrue} % 

\newif\iffontii\fontiifalse % 使用ctex设置字体
\DeclareOption{fontii}{\fontiitrue} % 

\newif\ifwinfont\winfontfalse 
\DeclareOption{winfont}{\winfonttrue} 

\newif\ifcwtxfont\cwtxfontfalse 
\DeclareOption{cwtxfont}{\cwtxfonttrue}

\newif\ifadobefont\adobefontfalse 
\DeclareOption{adobefont}{\adobefonttrue}

\newif\ifpres\presfalse % 使用xeCJK设置字体，
\DeclareOption{pres}{\prestrue} % 

\newif\ifprint\printfalse % 使用xeCJK设置字体，
\DeclareOption{print}{\printtrue} % 

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{beamer}}
\ProcessOptions
\LoadClass{beamer}

\mode<article> % 仅应用于article版本
{
  \RequirePackage{beamerbasearticle}
  \RequirePackage{fullpage}
  \RequirePackage{hyperref}
}
%% 加载几个常见sty packages
\RequirePackage{subfigure} %%图形或表格并排排列
\RequirePackage{xmpmulti}  %%支持文中的 \multiinclude 等命令, 使 mp 文件逐帧出现. 具体讨论见 beamer 手册.
\DeclareGraphicsRule{*}{mps}{*}{}
\RequirePackage{colortbl,dcolumn}%% 彩色表格
\RequirePackage{pgf,tikz,pgfarrows,pgfnodes,pgfautomata,pgfheaps}
\RequirePackage{amsmath,amssymb}
\RequirePackage{multimedia}
\RequirePackage{graphicx}%%插入图片
\RequirePackage{pgfpages}%抽取pdf文件中的某些页\includepdf[nup=2x2,landscape,delta=5mm 5mm,%scale=0.95,pages={1-18}]{trans.pdf}
\RequirePackage{textcomp}                % 千分号等特殊符号
\RequirePackage{bbding}                  % 一些特殊符号
\RequirePackage{txfonts}
\RequirePackage{pifont}
\RequirePackage{latexsym}
 %\RequirePackage{color,xcolor}            % 支持彩色文本、底色、文本框等
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\iffalse
\RequirePackage{wallpaper}
\RequirePackage{tikz}
\RequirePackage{eso-pic}
\newcommand\BackgroundPicture{%
   \put(0,0){%
     \parbox[b][\paperheight]{\paperwidth}{%
       \vfill
       \centering
       \includegraphics[width=0.95\paperwidth,height=0.95\paperheight,%
                        keepaspectratio]{fcc.jpg}%{rose3.eps}%
       \vfill
     }}}
%%%%%%%%%%%%%%
\newcommand\BackgroundPicturei{%
   \put(0,0){%
     \parbox[b][\paperheight]{\paperwidth}{%
       \vfill
      \centering
\color{red}
\vspace*{25.5cm}\rule{\textwidth}{1pt}\\*[1pt]
\rule[5mm]{\textwidth}{3pt}
       \vfill
     }}}
\fi
%\AddToShipoutPicture{\BackgroundPicture}%增加
%\ClearShipoutPicture%去掉
%%%%%%%%%%%%%字体设置%%%%%%%%%%%%%%%
\ifwinfont
\RequirePackage{fontspec}
\RequirePackage{xunicode}
\RequirePackage{xltxtra}
%\RequirePackage{fontspec,xunicode,xltxtra}%,beamerthemesplit}
%\RequirePackage[BoldFont={SimHei}, SlantFont={FangSong_GB2312}, CJKnumber]{xeCJK}
\RequirePackage[BoldFont, SlantFont, CJKnumber]{xeCJK}
\setmainfont[Mapping=tex-text]{Times New Roman}
\setsansfont{Arial}
\setmonofont{Courier New}

%\RequirePackage[BoldFont={SimHei}, SlantFont={FangSong_GB2312}, CJKnumber]{xeCJK} % xeCJK package
%\punctstyle{kaiming}
\punctstyle{hangmobanjiao}

%\defaultfontfeatures{Mapping=tex-text}
\XeTeXlinebreaklocale "zh" %采用中文断行方式
%\XeTeXlinebreakskip = 0pt plus 1pt %字元间可加入0pt~1pt 的弹性间距，这样才能排出左右对齐的段落。

\setCJKmainfont{SimSun}
\setCJKfamilyfont{song}{SimSun}
\setCJKfamilyfont{hei}{SimHei}
\setCJKfamilyfont{kai}{KaiTi_GB2312}%for winxp system
\setCJKfamilyfont{fang}{FangSong_GB2312}%for winxp system
%\setCJKfamilyfont{kai}{KaiTi}%for win8 system
%\setCJKfamilyfont{fang}{FangSong}%for win8 system
\setCJKfamilyfont{you}{YouYuan}
\setCJKfamilyfont{li}{LiSu}
%\setCJKfamilyfont{li}{LiSu}%for win8 system

\newcommand{\songti}{\CJKfamily{song}}
\newcommand{\heiti}{\CJKfamily{hei}}
\newcommand{\kaiti}{\CJKfamily{kai}}
\newcommand{\fangsong}{\CJKfamily{fang}}
\newcommand{\youyuan}{\CJKfamily{you}}
\newcommand{\lishu}{\CJKfamily{li}}%隶书
\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\ifcwtxfont
\RequirePackage{fontspec}
\RequirePackage{xunicode}
\RequirePackage{xltxtra}
%\RequirePackage{fontspec,xunicode,xltxtra}%,beamerthemesplit}
\RequirePackage[BoldFont, SlantFont, CJKnumber]{xeCJK} % xeCJK package
\setmainfont[Mapping=tex-text]{Times New Roman}%\rmfamily 使用的字体,默认英文和数字的字体。
\XeTeXlinebreaklocale "zh" %采用中文断行方式
%\XeTeXlinebreakskip = 0pt plus 1pt %字元间可加入0pt~1pt 的弹性间距，这样才能排出左右对齐的段落。

\setsansfont{Arial}
\setmonofont{Courier New}

\setCJKmainfont{cwTeXMing}%cwTeXMing 明体
\setCJKfamilyfont{song}{cwTeXMing}%cwTeXMing 明体
\setCJKfamilyfont{hei}{cwTeXHeiBold}%cwTeXHeiBold 粗黑体
\setCJKfamilyfont{kai}{cwTeXKai}%cwTeXKai 楷体
\setCJKfamilyfont{fang}{cwTeXFangSong}%cwTeXFangSong 仿宋
\setCJKfamilyfont{you}{cwTeXYen}%cwTeXYen 圆体
%\setCJKfamilyfont{li}{LiShu}

\newcommand{\songti}{\CJKfamily{song}}
\newcommand{\heiti}{\CJKfamily{hei}}
\newcommand{\kaiti}{\CJKfamily{kai}}
\newcommand{\fangsong}{\CJKfamily{fang}}
\newcommand{\youyuan}{\CJKfamily{you}}
%\newcommand{\lishu}{\CJKfamily{li}}%隶书
\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\ifadobefont
\RequirePackage{fontspec}
\RequirePackage{xunicode}
\RequirePackage{xltxtra}
%\RequirePackage{fontspec,xunicode,xltxtra}%,beamerthemesplit}
\RequirePackage[BoldFont, SlantFont, CJKnumber]{xeCJK}
\setmainfont[Mapping=tex-text]{Times New Roman}
\setsansfont{Arial}
\setmonofont{Courier New}

%\RequirePackage[BoldFont, SlantFont, CJKnumber]{xeCJK} % xeCJK package
%\setCJKmainfont[BoldFont={Adobe Heiti Std}, ItalicFont={Adobe Kaiti Std}]{Adobe Song Std}
\setCJKmainfont{Adobe Song Std}
\setCJKsansfont{Adobe Heiti Std}
\setCJKmonofont{Adobe Kaiti Std}
\punctstyle{hangmobanjiao}

  \setCJKfamilyfont{song}{Adobe Song Std}
  \setCJKfamilyfont{hei}{Adobe Heiti Std}
  \setCJKfamilyfont{fs}{Adobe Fangsong Std}
  \setCJKfamilyfont{kai}{Adobe Kaiti Std}
  \setCJKfamilyfont{li}{Adobe Kaiti Std} % todo: 用隶书字体代替
  \setCJKfamilyfont{you}{Adobe Kaiti Std} % todo: 用幼圆字体代替

  \setCJKfamilyfont{fhei}{AdobeFanHeitiStd-Bold}%方黑体
  \setCJKfamilyfont{ming}{AdobeMingStd-Light}%明细体
  \setCJKfamilyfont{myung}{AdobeMyungjoStd-Medium}

\newcommand{\songti}{\CJKfamily{song}} % 宋体
\newcommand{\heiti}{\CJKfamily{hei}}   % 黑体
\newcommand{\kaiti}{\CJKfamily{kai}}  % 楷书
\newcommand{\fangsong}{\CJKfamily{fs}} % 仿宋
\newcommand{\lishu}{\CJKfamily{li}}    % 隶书
\newcommand{\youyuan}{\CJKfamily{you}} % 幼圆

\newcommand{\fangsonghei}{\CJKfamily{fhei}} % 仿宋黑体
\newcommand{\mingti}{\CJKfamily{ming}} % 仿宋黑体
\newcommand{\adobezw}{\CJKfamily{myung}} %adobe中文
\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\iffonti
\RequirePackage{fontspec}
\RequirePackage{xunicode}
\RequirePackage{xltxtra}
%\RequirePackage[BoldFont={SimHei}, SlantFont={FangSong_GB2312}, CJKnumber]{xeCJK} % xeCJK package
%\RequirePackage{fontspec,xunicode,xltxtra}%,beamerthemesplit}
\RequirePackage[BoldFont, SlantFont, CJKnumber]{xeCJK}
%\punctstyle{kaiming}
\punctstyle{hangmobanjiao}

\setmainfont[Mapping=tex-text]{Times New Roman}
\setsansfont{Arial}
\setmonofont{Courier New}

%\defaultfontfeatures{Mapping=tex-text}

\XeTeXlinebreaklocale "zh" %采用中文断行方式
\XeTeXlinebreakskip = 0pt plus 1pt %字元间可加入0pt~1pt 的弹性间距，这样才能排出左右对齐的段落。

\setCJKmainfont{SimSun}
\setCJKfamilyfont{song}{SimSun}
\setCJKfamilyfont{hei}{SimHei}
\setCJKfamilyfont{kai}{KaiTi_GB2312}%for winxp system
\setCJKfamilyfont{fang}{FangSong_GB2312}%for winxp system
%\setCJKfamilyfont{kai}{KaiTi}%for win8 system
%\setCJKfamilyfont{fang}{FangSong}%for win8 system
\setCJKfamilyfont{you}{YouYuan}
\setCJKfamilyfont{li}{LiSu}
%\setCJKfamilyfont{li}{LiSu}%for win8 system

\newcommand{\fangsong}{\CJKfamily{fang}}
\newcommand{\songti}{\CJKfamily{song}}
\newcommand{\heiti}{\CJKfamily{hei}}
\newcommand{\kaiti}{\CJKfamily{kai}}
\newcommand{\youyuan}{\CJKfamily{you}}
\newcommand{\lishu}{\CJKfamily{li}}%隶书
\setCJKfamilyfont{fzxbs}{方正小标宋简体}
\newcommand{\fzxbs}{\CJKfamily{fzxbs}}

\setCJKfamilyfont{hwsong}{STSong} %华文宋体  hwsong
\newcommand{\hwsongti}{\CJKfamily{hwsong}}
\setCJKfamilyfont{hwzs}{STZhongsong} %华文中宋  hwzs
\newcommand{\hwzhongsong}{\CJKfamily{hwzs}}
\setCJKfamilyfont{hwfs}{STFangsong}%华文仿宋  hwfs
\newcommand{\hwfangsong}{\CJKfamily{hwfs}}
\setCJKfamilyfont{hwxh}{STXihei}%华文细黑  hwxh
\newcommand{\hwxihei}{\CJKfamily{hwxh}}
\setCJKfamilyfont{hwl}{STLiti}%华文隶书  hwl
\newcommand{\hwlishu}{\CJKfamily{hwl}}
\setCJKfamilyfont{hwxw}{STXinwei} %华文新魏  hwxw
\newcommand{\hwxinwei}{\CJKfamily{hwxw}}
\setCJKfamilyfont{hwk}{STKaiti}%华文楷体  hwk
\newcommand{\hwkaiti}{\CJKfamily{hwk}}
\setCJKfamilyfont{hwxk}{STXingkai}%华文行楷  hwxk
\newcommand{\hwxingkai}{\CJKfamily{hwxk}}
\setCJKfamilyfont{hwcaiyun}{STCaiyun}%华文彩云 hwcy
\newcommand{\hwcy}{\CJKfamily{hwcy}}
\setCJKfamilyfont{hwhupo}{STHupo} %华文琥珀   hwhp
\newcommand{\hwhp}{\CJKfamily{hwhp}}
\setCJKfamilyfont{yh}{Microsoft YaHei}
\newcommand{\yahei}{\CJKfamily{yh}}
\setCJKfamilyfont{fzsong}{Simsun (Founder Extended)}%方正宋体超大字符集   fzsong
\newcommand{\fzsongti}{\CJKfamily{fzsong}}
\setCJKfamilyfont{fzyao}{FZYaoTi}%方正姚体  fzy
\newcommand{\fzyaoti}{\CJKfamily{fzyao}}
\setCJKfamilyfont{fzshu}{FZShuTi} %方正舒体 fzshu
\newcommand{\fzshuti}{\CJKfamily{fzshu}}
\setCJKfamilyfont{asong}{Adobe Song Std} %Adobe 宋体  asong
\newcommand{\asongti}{\CJKfamily{asong}}
\setCJKfamilyfont{ahei}{Adobe Heiti Std}%Adobe 黑体  ahei
\newcommand{\aheiti}{\CJKfamily{ahei}}
\setCJKfamilyfont{akai}{Adobe Kaiti Std}%Adobe 楷体  akai
\newcommand{\akaiti}{\CJKfamily{akai}}
\setCJKfamilyfont{afs}{Adobe Fangsong Std}
\newcommand{\afangsong}{\CJKfamily{afs}}

\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\iffontii%ctex font use pdflatex for compile
\RequirePackage[UTF8]{ctex}
\RequirePackage{times}

\newcommand{\song}{\CJKfamily{song}}    % 宋体   (Windows自带simsun.ttf)
\newcommand{\fs}{\CJKfamily{fs}}        % 仿宋体 (Windows自带simfs.ttf)
\newcommand{\kai}{\CJKfamily{kai}}      % 楷体   (Windows自带simkai.ttf)
\newcommand{\hei}{\CJKfamily{hei}}      % 黑体   (Windows自带simhei.ttf)
\newcommand{\li}{\CJKfamily{li}}        % 隶书   (Windows自带simli.ttf)
\newcommand{\you}{\CJKfamily{you}}      %幼圆   (Windows 自带simyou.ttf)

\renewcommand*{\songti}{\song}
\renewcommand*{\fangsong}{\fs}
\newcommand*{\kaiti}{\kai}
\renewcommand*{\heiti}{\hei}
\renewcommand*{\lishu}{\li}
\renewcommand*{\youyuan}{\you}

\newcommand*{\fzxbs}{\hei}
\fi

%\addtocounter{enumi}{1}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\iffalse
\newcommand{\linespacing}[1]{\linespread{#1}\selectfont}% 行距命令
%%%%%%%------------------
\newcommand{\todayCN}{\the\year~年~\the\month~月~\the\day~日}
\newcommand{\gdhstline}{\parindent=0pt \textcolor{red}{\rule[5mm]{\textwidth}{3pt}\\*[-40pt]\rule{\textwidth}{1pt}}}
\newcommand{\gdhstitle}{\begin{center}{\parindent=0pt \textcolor{red}{\erhao\fzxbs 广东华隧建设股份有限公司}\\ \gdhstline}\end{center}}
\newcommand{\gdhsbline}{\parindent=0pt \textcolor{red}{\rule{\textwidth}{1pt}}\\*[-40pt]\rule[5mm]{\textwidth}{3pt}}
\fi
\endinput
%%%
%%%%%%%%%%%%%%%%%%%%%%%%% End of file `gdhsppt.cls'.
