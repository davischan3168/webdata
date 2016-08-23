\NeedsTeXFormat{LaTeX2e}[1999/12/01]
\ProvidesClass{gdhsarticle}[2011/03/31 2.0.1 The LaTeX class for the course paper of South China University of Technology]
%% import global options
\newif\ifmasterdegree\masterdegreefalse %默认为doctor
\newif\ifpdfcover\pdfcoverfalse

\newif\ifdraftmode\draftmodefalse % ad初稿加上水印背景
\DeclareOption{draftmode}{\draftmodetrue} % a

\newif\iffonti\fontifalse % 使用xeCJK设置字体，
\DeclareOption{fonti}{\fontitrue} % 

\newif\iffontiii\fontiiifalse % for gdhs only
\DeclareOption{fontiii}{\fontiiitrue} % 

\newif\iffontii\fontiifalse % 使用ctex设置字体
\DeclareOption{fontii}{\fontiitrue} % 

\newif\iffewfont\fewfontfalse % 使用xeCJK设置字体，
\DeclareOption{fewfont}{\fewfonttrue} % fewfont 

\newif\ifwinfont\winfontfalse 
\DeclareOption{winfont}{\winfonttrue} 

\newif\ifcwtxfont\cwtxfontfalse 
\DeclareOption{cwtxfont}{\cwtxfonttrue}

\newif\ifadobefont\adobefontfalse 
\DeclareOption{adobefont}{\adobefonttrue}

\newif\ifadobefontv\adobefontvfalse 
\DeclareOption{adobefontv}{\adobefontvtrue}

\newif\ifmyzhmcjk\myzhmcjkfalse 
\DeclareOption{myzhmcjk}{\myzhmcjktrue}

\newif\ifmyxecjk\myxecjkfalse 
\DeclareOption{myxecjk}{\myxecjktrue}

\newif\ifmemo\memofalse 
\DeclareOption{memo}{\memotrue}

\newif\ifxieyibk\xieyibkfalse 
\DeclareOption{xieyibk}{\xieyibktrue}

\newif\ifmsize\msizefalse 
\DeclareOption{msize}{\msizetrue}

\newif\iftexsize\texsizefalse 
\DeclareOption{texsize}{\texsizetrue}

\DeclareOption{master}{\masterdegreetrue}
\DeclareOption{pdfcover}{\pdfcovertrue} %using pdfcover,TOdo

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions
\LoadClass[12pt]{article}

\newif\ifonepage\onepagetrue

%% define 引入配置文件
\newcommand{\scutthesis}{%
  S\hspace{-0.3ex}\raisebox{-0.5ex}{C}\hspace{-0.3ex}U\hspace{0.1em}\raisebox{-0.5ex}{T}%
  \textsc{Thesis} }
\ifmasterdegree \newcommand{\@degree}{硕士} \else \newcommand{\@degree}{博士} \fi
\newcommand{\thesissubject}{我的article模板}%{华南理工大学\@degree{}课程论文}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\RequirePackage{ifpdf}
\RequirePackage{ifthen}
%\RequirePackage{graphicx}
\RequirePackage{doc}
\RequirePackage{keyval}
%\RequirePackage[dvipsnames,table]{xcolor}
\RequirePackage{indentfirst}
\RequirePackage{makeidx} % 索引
\RequirePackage{amsmath}
%\RequirePackage[final]{pdfpages}
%%%%%我的包
\RequirePackage{footnote}%改进了标准的LaTeX2e的\footnote命令，使得可以在\parbox,minipage和table环境中标记的脚注能够被正确地放置在整个页面的下方脚注区中。
%\RequirePackage{labels}
\RequirePackage{fancybox}%提供了\shadowbox,\doublebox,\ovalbox和\Ovalbox四个命令来生成不同形状的盒子。
%%%%%%%%%%%%%%%%%表格
\RequirePackage{threeparttable}
\RequirePackage{colortbl,dcolumn,fancyref}
\RequirePackage{diagbox}%可在表格的单元格中画上一斜线。
\RequirePackage{multirow}%如果表各种某一单元横跨两行以上，就要用multirow了
\RequirePackage{booktabs}%让你的表格中使用不同粗细的横线来划分行。
\RequirePackage{longtable}%如果表格太长，超过了一页时，就可以试试longtable宏包所定义的longtable环境
\RequirePackage{tabularx}%提供了新的表格环境tabular*、tabularx，可以设定表格的宽度。
\RequirePackage{supertabular}%自动计算表格的高度，把超出页面的表格部分放置在下一页。
\RequirePackage{array} % 扩展了 array 和 tabular 环境功能
%%%%%%%%%%%%%%%%%%%%%%%%%%%
\RequirePackage{rotating}
\RequirePackage{lscape}%页面横排\begin{landscape}***\end{landscape}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\RequirePackage{textcomp}%千分号等特殊符号
\RequirePackage{bbding}%一些特殊符号
%\RequirePackage{cite}%支持引用
\RequirePackage{color,xcolor}%支持彩色文本、底色、文本框等
\RequirePackage{calc}%使用latex计算功能
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{lastpage}
\RequirePackage{draftcopy}%[timestamp,first]{draftcopy}
%\draftcopyName{IloveTeX}{130}%利用draftcopy做水印
%\draftcopyFirstPage{2}%draftcopy开始页码
%\draftcopyLastPage{2}%draftcopy结束页码
%\draftcopySetGrey{0.8}%数越小灰度越大
%\draftcopyVersion{Version2.0}
\RequirePackage{wallpaper}
\RequirePackage{tikz}
\RequirePackage{eso-pic}
%\AddToShipoutPicture{\BackgroundPicture}%这一页开始水印背景
%\ClearShipoutPicture%这一页终止水印背景.
\newcommand\BackgroundPicture{%
   \put(0,0){%
     \parbox[b][\paperheight]{\paperwidth}{%
       \vfill
       \centering
       \includegraphics[width=0.95\paperwidth,height=0.95\paperheight,%
                        keepaspectratio]{rose3.eps}%
       \vfill
     }}}
%%%%%%%%%%%%%%
%%%水印设置三
\ifdraftmode 
   \RequirePackage{draftwatermark} %  added by Quansheng Guan, 初稿加上水印背景
        \SetWatermarkAngle{60}
        \SetWatermarkLightness{0.75}
        \SetWatermarkFontSize{3cm}
        \SetWatermarkScale{1}
        \SetWatermarkText{初~~稿\sanhao \today}%\small\today}
\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\RequirePackage{graphics}
\RequirePackage{graphicx}%%插入图片
\DeclareGraphicsRule{*}{eps}{*}{}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\RequirePackage{pdfpages}%抽取pdf文件中的某些页\includepdf[nup=2x2,landscape,delta=5mm5mm,%scale=0.95,pages={1-18}]{trans.pdf}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\RequirePackage{textcomp}%千分号等特殊符号
\RequirePackage{bbding}%一些特殊符号
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\RequirePackage[left=3cm,right=2cm,bottom=2.5cm,top=2.5cm,%设置页面上下左右
 headheight=1.5cm,%页眉所占高度
 footskip=1cm %页脚所占高度
]{geometry}
\RequirePackage{enumitem}
\RequirePackage{color,xcolor}%支持彩色文本、底色、文本框等
\RequirePackage[unicode=true,
          bookmarks=true,
          bookmarksnumbered=true,
          bookmarksopen=false,
          breaklinks=false,
          pdfborder={0 0 1},
          backref=false,
          colorlinks=true]{hyperref}
%%%%%%%%%%%%%%%%%%%%%5% Code
\RequirePackage{listings}
\lstset{
    basicstyle=\wuhao,
    extendedchars=true,
    keywordstyle=\color{blue!70},
    commentstyle=\color{red!50!green!50!blue!50}, 
    showspaces=false,          % 显示空格
    showstringspaces=false,    % 字符串中显示空格
    showtabs=false,            % 显示 TAB
    tabsize=2,                 % TAB 被当作两个空格
    captionpos=b,              % 标题位置
    breaklines=true,           % 自动断行
    breakatwhitespace=false,   
    escapeinside={\%*}{*)}
}
%%%%%%%%%%%%%字体设置
\iffewfont 
\RequirePackage[BoldFont, SlantFont, CJKnumber]{xeCJK} % xeCJK package
%\punctstyle{kaiming}
\setmainfont[Mapping=tex-text]{Times New Roman}%\rmfamily 使用的字体,默认英文和数字的字体。
\XeTeXlinebreaklocale "zh" %采用中文断行方式
\XeTeXlinebreakskip = 0pt plus 1pt %字元间可加入0pt~1pt 的弹性间距，这样才能排出左右对齐的段落。
\RequirePackage{CJKnumb}
%\setmainfont{Times New Roman}
\setsansfont{Arial}
\setmonofont{Courier New}

\setCJKmainfont{FangSong_GB2312}%{SimSun}
\setCJKsansfont{SimHei}
\setCJKmonofont{KaiTi_GB2312}

\setCJKfamilyfont{song}{SimSun}
\setCJKfamilyfont{hei}{SimHei}
\setCJKfamilyfont{kai}{KaiTi_GB2312}
\setCJKfamilyfont{fang}{FangSong_GB2312}
\setCJKfamilyfont{you}{YouYuan}
\setCJKfamilyfont{li}{LiSu}

\newcommand{\songti}{\CJKfamily{song}}
\newcommand{\heiti}{\CJKfamily{hei}}
\newcommand{\kaiti}{\CJKfamily{kai}}
\newcommand{\fangsong}{\CJKfamily{fang}}
\newcommand{\youyuan}{\CJKfamily{you}}
\newcommand{\lishu}{\CJKfamily{li}}%隶书

\setCJKfamilyfont{fzxbs}{方正小标宋简体}
\newcommand{\fzxbs}{\CJKfamily{fzxbs}}
\newcommand{\fzxiaobaosong}{\CJKfamily{fzxbs}}
\setCJKfamilyfont{fzsong}{Simsun (Founder Extended)}     %方正宋体超大字符集   fzsong
\newcommand{\fzsongtida}{\CJKfamily{fzsong}}
\setCJKfamilyfont{fzyao}{FZYaoTi}                                    %方正姚体  fzy
\newcommand{\fzyaoti}{\CJKfamily{fzyao}}
\setCJKfamilyfont{fzshu}{FZShuTi}                                    %方正舒体 fzshu
\newcommand{\fzshuti}{\CJKfamily{fzshu}}

\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\ifwinfont
\RequirePackage[BoldFont, SlantFont, CJKnumber]{xeCJK} % xeCJK package
%\punctstyle{kaiming}
\setmainfont[Mapping=tex-text]{Times New Roman}%\rmfamily 使用的字体,默认英文和数字的字体。
\XeTeXlinebreaklocale "zh" %采用中文断行方式
\XeTeXlinebreakskip = 0pt plus 1pt %字元间可加入0pt~1pt 的弹性间距，这样才能排出左右对齐的段落。
\RequirePackage{CJKnumb}
%\setmainfont{Times New Roman}
\setsansfont{Arial}
\setmonofont{Courier New}

\setCJKmainfont{SimSun}
\setCJKsansfont{SimHei}
\setCJKmonofont{KaiTi_GB2312}

\setCJKfamilyfont{song}{SimSun}
\setCJKfamilyfont{hei}{SimHei}
\setCJKfamilyfont{kai}{KaiTi_GB2312}
\setCJKfamilyfont{fang}{FangSong_GB2312}
\setCJKfamilyfont{you}{YouYuan}
\setCJKfamilyfont{li}{LiSu}

\newcommand{\songti}{\CJKfamily{song}}
\newcommand{\heiti}{\CJKfamily{hei}}
\newcommand{\kaiti}{\CJKfamily{kai}}
\newcommand{\fangsong}{\CJKfamily{fang}}
\newcommand{\youyuan}{\CJKfamily{you}}
\newcommand{\lishu}{\CJKfamily{li}}%隶书
\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\ifcwtxfont 
\RequirePackage[BoldFont, SlantFont, CJKnumber]{xeCJK} % xeCJK package
%\punctstyle{kaiming}
\setmainfont[Mapping=tex-text]{Times New Roman}%\rmfamily 使用的字体,默认英文和数字的字体。
\XeTeXlinebreaklocale "zh" %采用中文断行方式
\XeTeXlinebreakskip = 0pt plus 1pt %字元间可加入0pt~1pt 的弹性间距，这样才能排出左右对齐的段落。
\RequirePackage{CJKnumb}
%\setmainfont{Times New Roman}
\setsansfont{Arial}
\setmonofont{Courier New}

\setCJKmainfont{cwTeXMing}%cwTeXMing 明体
\setCJKfamilyfont{song}{cwTeXMing}%cwTeXMing 明体
\setCJKfamilyfont{hei}{cwTeXHeiBold}%cwTeXHeiBold 粗黑体
\setCJKfamilyfont{kai}{cwTeXKai}%cwTeXKai 楷体
\setCJKfamilyfont{fang}{cwTeXFangSong}%cwTeXFangSong 仿宋
\setCJKfamilyfont{you}{cwTeXYen}%cwTeXYen 圆体
%\setCJKfamilyfont{li}{LiSu}

\newcommand{\songti}{\CJKfamily{song}}
\newcommand{\heiti}{\CJKfamily{hei}}
\newcommand{\kaiti}{\CJKfamily{kai}}
\newcommand{\fangsong}{\CJKfamily{fang}}
\newcommand{\youyuan}{\CJKfamily{you}}
%\newcommand{\lishu}{\CJKfamily{li}}%隶书
\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\ifadobefont 
\RequirePackage[BoldFont, SlantFont, CJKnumber]{xeCJK} % xeCJK package
%\punctstyle{kaiming}
\setmainfont[Mapping=tex-text]{Times New Roman}%\rmfamily 使用的字体,默认英文和数字的字体。
\XeTeXlinebreaklocale "zh" %采用中文断行方式
\XeTeXlinebreakskip = 0pt plus 1pt %字元间可加入0pt~1pt 的弹性间距，这样才能排出左右对齐的段落。
\RequirePackage{CJKnumb}
%\setmainfont{Times New Roman}
\setsansfont{Arial}
\setmonofont{Courier New}

  \setCJKmainfont[BoldFont={Adobe Heiti Std}, ItalicFont={Adobe Kaiti Std}]{Adobe Song Std}
  \setCJKsansfont{Adobe Heiti Std}
  \setCJKmonofont{Adobe Kaiti Std}

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
\RequirePackage[BoldFont, SlantFont, CJKnumber]{xeCJK} % xeCJK package
%\punctstyle{kaiming}
\setmainfont[Mapping=tex-text]{Times New Roman}%\rmfamily 使用的字体,默认英文和数字的字体。
\XeTeXlinebreaklocale "zh" %采用中文断行方式
\XeTeXlinebreakskip = 0pt plus 1pt %字元间可加入0pt~1pt 的弹性间距，这样才能排出左右对齐的段落。
\RequirePackage{CJKnumb}
%\setmainfont{Times New Roman}
\setsansfont{Arial}
\setmonofont{Courier New}

\setCJKmainfont{SimSun}%{FangSong_GB2312}%{SimSun}
\setCJKsansfont{SimHei}
\setCJKmonofont{KaiTi_GB2312}

\setCJKfamilyfont{song}{SimSun}
\setCJKfamilyfont{hei}{SimHei}
\setCJKfamilyfont{kai}{KaiTi_GB2312}
\setCJKfamilyfont{fang}{FangSong_GB2312}
\setCJKfamilyfont{you}{YouYuan}
\setCJKfamilyfont{li}{LiSu}

\newcommand{\songti}{\CJKfamily{song}}
\newcommand{\heiti}{\CJKfamily{hei}}
\newcommand{\kaiti}{\CJKfamily{kai}}
\newcommand{\fangsong}{\CJKfamily{fang}}
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
\newcommand{\hwxinhei}{\CJKfamily{hwxh}}
\setCJKfamilyfont{hwl}{STLiti}%华文隶书  hwl
\newcommand{\hwlishu}{\CJKfamily{hwl}}
\setCJKfamilyfont{hwxw}{STXinwei} %华文新魏  hwxw
\newcommand{\hwxinwei}{\CJKfamily{hwxw}}
\setCJKfamilyfont{hwk}{STKaiti}%华文楷体  hwk
\newcommand{\hwkaiti}{\CJKfamily{hwk}}
\setCJKfamilyfont{hwxk}{STXingkai}%华文行楷  hwxk
\newcommand{\hwxingkai}{\CJKfamily{hwxk}}
\setCJKfamilyfont{hwcy}{STCaiyun}%华文彩云 hwcy
\newcommand{\hwcaiyun}{\CJKfamily{hwcy}}
\setCJKfamilyfont{hwhp}{STHupo} %华文琥珀   hwhp
\newcommand{\hwhupo}{\CJKfamily{hwhp}}
\setCJKfamilyfont{yh}{Microsoft YaHei}
\newcommand{\yahei}{\CJKfamily{yh}}
\setCJKfamilyfont{fzsong}{Simsun (Founder Extended)}%方正宋体超大字符集   fzsong
\newcommand{\fzsongtida}{\CJKfamily{fzsong}}
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
%\RequirePackage{paralist}% 修改列表格式
%\setdefaultenum{1)}{a)}{i.}{A.}% 设置列表模式,for \enumerate
%\setdefaultenum{\heiti\bf{第\CJKnumber{\arabic{enumi}}条}}{a)}{i.}{A.}
%\setdefaultleftmargin{4ex}{}{}{}{}{}%standard \itemize :• – ∗ ·
\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\iffontii%ctex font use pdflatex for compile
\RequirePackage[UTF8]{ctex}
\RequirePackage{times}
\RequirePackage{CJKnumb}
%\RequirePackage[mtbold,mtpluscal,mtplusscr]{mathtime}

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

\newcommand*{\fzxbs}{\heiti\bfseries}
\newcommand*{\fzxiaobaosong}{\heiti\bfseries}
\newcommand*{\hwzs}{\songti\bfseries}
\newcommand*{\hwzhongsong}{\songti\bfseries}


%\providecommand{\CJKnumber}[1]{\ifcase#1\or{一}\or{二}\or{三}\or{四}\or{五}\or{六}\or{七}\or{八}\or{九}\or{十}\fi}
%\newcommand{\CJKnumber}[1]{\ifcase#1\or{一}\or{二}\or{三}\or{四}\or{五}\or{六}\or{七}\or{八}\or{九}\or{十}\fi}
\iffalse
\@ifundefined{CJKnumber}
  {\def\CJKnumber#1{\ifcase#1\or
                    一\or二\or三\or四\or五\or
                    六\or七\or八\or九\or十\or十一\or十二\or十三\or十四\or十五\fi}}{}
                    \fi
\fi
%%%%%%%%%%%%%5%%%%
\iffontiii% use fontsepc to set CHinese font, use xelatex compile.
%\usepackage{zhmCJK}
%\RequirePackage{CJK}
\RequirePackage{zhmCJK}
\RequirePackage{times}
\RequirePackage{CJKnumb}

\setCJKmainfont[BoldFont=simhei.ttf,ItalicFont=simkai.ttf]{simsun.ttc}
\setCJKsansfont[AutoFakeBold=0]{simhei.ttf}
\setCJKmonofont[AutoFakeSlant]{simfang.ttf}

\setCJKfamilyfont{fang}{simfang.ttf}
\setCJKfamilyfont{song}{simsun.ttc}
\setCJKfamilyfont{hei}{simhei.ttf}
\setCJKfamilyfont{kai}{simkai.ttf}
\setCJKfamilyfont{you}{simyou.ttf}
\setCJKfamilyfont{li}{simli.ttf}
\setCJKfamilyfont{yahei}[BoldFont=msyhbd.ttf]{msyh.ttf}

\newcommand{\songti}{\CJKfamily{song}}
\newcommand{\heiti}{\CJKfamily{hei}}
\newcommand{\kaiti}{\CJKfamily{kai}}
\newcommand{\fangsong}{\CJKfamily{fang}}
\newcommand{\youyuan}{\CJKfamily{you}}
\newcommand{\lishu}{\CJKfamily{li}}%隶书
\newcommand{\yahei}{\CJKfamily{yahei}}

\setCJKfamilyfont{hwsongti}{STSONG.TTF} %华文宋体  hwsong
\newcommand{\hwsongti}{\CJKfamily{hwsongti}}
\setCJKfamilyfont{hwzhongsong}{STZHONGS.TTF} %华文中宋  hwzs
\newcommand{\hwzhongsong}{\CJKfamily{hwzhongsong}}
\setCJKfamilyfont{hwfangsong}{STFANGSO.TTF}%华文仿宋  hwfs
\newcommand{\hwfangsong}{\CJKfamily{hwfangsong}}
\setCJKfamilyfont{hwxihei}{STXIHEI.TTF}%华文细黑  hwxh
\newcommand{\hwxihei}{\CJKfamily{hwxihei}}
\setCJKfamilyfont{hwlishu}{STLiti.ttf}%华文隶书  hwl
\newcommand{\hwlishu}{\CJKfamily{hwlishu}}
\setCJKfamilyfont{hwxinwei}{STXinwei.ttf} %华文新魏  hwxw
\newcommand{\hwxinwei}{\CJKfamily{hwxiwei}}
\setCJKfamilyfont{hwkaiti}{STKaiti.ttf}%华文楷体  hwk
\newcommand{\hwkaiti}{\CJKfamily{hwkaiti}}
\setCJKfamilyfont{hwxingkai}{STXingka.ttf}%华文行楷  hwxk
\newcommand{\hwxingkai}{\CJKfamily{hwxingkai}}
\setCJKfamilyfont{hwcaiyun}{STCaiyun.ttf}%华文彩云 hwcy
\newcommand{\hwcaiyun}{\CJKfamily{hwcaiyun}}
\setCJKfamilyfont{hwhupo}{STHupo.ttf} %华文琥珀   hwhp
\newcommand{\hwhupo}{\CJKfamily{hwhupo}}

\setCJKfamilyfont{fzxbs}{FZXBSJW.TTF}
\newcommand{\fzxbs}{\CJKfamily{fzxbs}}
%\providecommand{\CJKnumber}[1]{\ifcase#1\or{一}\or{二}\or{三}\or{四}\or{五}\or{六}\or{七}\or{八}\or{九}\or{十}\fi}
\@ifundefined{CJKnumber}
  {\def\CJKnumber#1{\ifcase#1\or
                    一\or二\or三\or四\or五\or
                    六\or七\or八\or九\or十\or十一\or十二\or十三\or十四\or十五\fi}}{}

\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\ifmyzhmcjk

\RequirePackage{zhmCJK}
\RequirePackage{times}
\RequirePackage{CJKnumb}

\setCJKmainfont[BoldFont=simhei.ttf,ItalicFont=simkai.ttf]{simsun.ttc}
\setCJKsansfont[AutoFakeBold=0]{simhei.ttf}
\setCJKmonofont[AutoFakeSlant]{simfang.ttf}

\setCJKfamilyfont{fang}{simfang.ttf}
\setCJKfamilyfont{song}{simsun.ttc}
\setCJKfamilyfont{hei}{simhei.ttf}
\setCJKfamilyfont{kai}{simkai.ttf}
\setCJKfamilyfont{you}{simyou.ttf}
\setCJKfamilyfont{li}{simli.ttf}
\setCJKfamilyfont{yahei}[BoldFont=msyhbd.ttf]{msyh.ttf}

\newcommand{\songti}{\CJKfamily{song}}
\newcommand{\heiti}{\CJKfamily{hei}}
\newcommand{\kaiti}{\CJKfamily{kai}}
\newcommand{\fangsong}{\CJKfamily{fang}}
\newcommand{\youyuan}{\CJKfamily{you}}
\newcommand{\lishu}{\CJKfamily{li}}%隶书
\newcommand{\yahei}{\CJKfamily{yahei}}
%\newcommand{\xinwei}{\CJKfamily{xinwei}}


%huawenziti
\setCJKfamilyfont{hwxihei}{STXIHEI.TTF}
\newcommand{\hwxihei}{\CJKfamily{hwxihei}}
\setCJKfamilyfont{hwxinwei}{STXINWEI.TTF}
\newcommand{\hwxinwei}{\CJKfamily{hwxinwei}}
\setCJKfamilyfont{hwfangsong}{STFANGSO.TTF}
\newcommand{\hwfangsong}{\CJKfamily{hwfangsong}}
\setCJKfamilyfont{hwxingkai}{STXINGKA.TTF}
\newcommand{\hwxingkai}{\CJKfamily{hwxingkai}}
\setCJKfamilyfont{hwzhongsong}{STZHONGS.TTF}
\newcommand{\hwzhongsong}{\CJKfamily{hwzhongsong}}
\setCJKfamilyfont{hwhupo}{STHUPO.TTF}
\newcommand{\hwhupo}{\CJKfamily{hwhupo}}
\setCJKfamilyfont{hwkaiti}{STKAITI.TTF}
\newcommand{\hwkaiti}{\CJKfamily{hwkaiti}}
\setCJKfamilyfont{hwcaiyun}{STCAIYUN.TTF}
\newcommand{\hwcaiyun}{\CJKfamily{hwcaiyun}}
\setCJKfamilyfont{hwsongti}{STSONG.TTF}
\newcommand{\hwsongti}{\CJKfamily{hwsongti}}
\setCJKfamilyfont{hwlishu}{STLITI.TTF}
\newcommand{\hwlishu}{\CJKfamily{hwlishu}}

%fangzhengziti

\setCJKfamilyfont{fzxbs}{FZXBSJW.TTF}%方正小标宋
\newcommand{\fzxbs}{\CJKfamily{fzxbs}}
\newcommand{\fzxiaobaosong}{\CJKfamily{fzxbs}}
\setCJKfamilyfont{fzyinbixingshuj}{FZYBXSJW.TTF}
\newcommand{\fzyinbixingshuj}{\CJKfamily{fzyinbixingshuj}}
\setCJKfamilyfont{fzyinbikaishuj}{FZYBKSJW.TTF}
\newcommand{\fzyinbikaishuj}{\CJKfamily{fzyinbikaishuj}}
\setCJKfamilyfont{fzcaiyunj}{FZCYJW.TTF}
\newcommand{\fzcaiyunj}{\CJKfamily{fzcaiyunj}}
\setCJKfamilyfont{fzshutij}{FZSTJW.TTF}
\newcommand{\fzheipingpf}{\CJKfamily{fzheipingpf}}
\setCJKfamilyfont{fzyaoti}{FZYTK.TTF}
\newcommand{\fzyaoti}{\CJKfamily{fzyaoti}}
\setCJKfamilyfont{fzkaitij}{FZKTJW.TTF}
\newcommand{\fzkaitij}{\CJKfamily{fzkaitij}}
\setCJKfamilyfont{fzchusongj}{FZCSJW.TTF}
\newcommand{\fzchusongj}{\CJKfamily{fzchusongj}}
\setCJKfamilyfont{fzdabiaosongj}{FZDBSJW.TTF}
\newcommand{\fzdabiaosongj}{\CJKfamily{fzdabiaosongj}}
\setCJKfamilyfont{fzsongheij}{FZSHJW.TTF}
\newcommand{\fzsongheij}{\CJKfamily{fzsongheij}}
\setCJKfamilyfont{fzxiaozhuanti}{FZXZTFW.TTF}
\newcommand{\fzxiaozhuanti}{\CJKfamily{fzxiaozhuanti}}
\setCJKfamilyfont{fzxinbaosongj}{FZNBSJW.TTF}
\newcommand{\fzxinbaosongj}{\CJKfamily{fzxinbaosongj}}
\setCJKfamilyfont{fzqitij}{FZQTJW.TTF}
\newcommand{\fzqitij}{\CJKfamily{fzqitij}}
\setCJKfamilyfont{fztechughj}{FZTCGHJW.TTF}
\newcommand{\fztechughj}{\CJKfamily{fztechughj}}
\iffalse
\setCJKfamilyfont{fzshaoerj}{FZSEJW.TTF}
\newcommand{\fzshaoerj}{\CJKfamily{fzshaoerj}}
\setCJKfamilyfont{fzdaheij}{FZDHTJW.TTF}
\newcommand{\fzdaheij}{\CJKfamily{fzdaheij}}
\setCJKfamilyfont{fzzhengsongsanj}{FZS3JW.TTF}
\newcommand{\fzzhengsongsanj}{\CJKfamily{fzzhengsongsanj}}
\setCJKfamilyfont{fztechughj}{FZTCGHJW.TTF}
\newcommand{\fzshaoerj}{\CJKfamily{fzshaoerj}}
\setCJKfamilyfont{fzzhengkaij}{FZXKJW.TTF}
\newcommand{\fzzhengkaij}{\CJKfamily{fzzhengkaij}}
\setCJKfamilyfont{fzzongyij}{FZZYJW.TTF}
\newcommand{\fzzongyij}{\CJKfamily{fzzongyij}}
\setCJKfamilyfont{fzsuxinshiliukaij}{FZSXSLKJW.TTF}
\newcommand{\fzsuxinshiliukaij}{\CJKfamily{fzsuxinshiliukaij}}
\setCJKfamilyfont{fzshuiheij}{FZSHHJW.TTF}
\newcommand{\fzshuiheij}{\CJKfamily{fzshuiheij}}
\setCJKfamilyfont{fzxiyuanj}{FZY1JW.TTF}
\newcommand{\fzxiyuanj}{\CJKfamily{fzxiyuanj}}
\setCJKfamilyfont{fzxidengxianj}{FZXDXJW.TTF}
\newcommand{\fzxidengxianj}{\CJKfamily{fzxidengxianj}}
\setCJKfamilyfont{fzxiheiyij}{FZXH1JW.TTF}
\newcommand{\fzxiheiyij}{\CJKfamily{fzxiheiyij}}
\setCJKfamilyfont{fzgulij}{FZGLJW.TTF}
\newcommand{\fzgulij}{\CJKfamily{fzgulij}}
\setCJKfamilyfont{fzpangtouyuj}{FZPTYJW.TTF}
\newcommand{\fzpangtouyuj}{\CJKfamily{fzpangtouyuj}}
\setCJKfamilyfont{fzyouxianj}{FZYXJW.TTF}
\newcommand{\fzyouxianj}{\CJKfamily{fzyouxianj}}
\setCJKfamilyfont{fzkangtij}{FZKANGJW.TTF}
\newcommand{\fzkangtij}{\CJKfamily{fzkangtij}}
\setCJKfamilyfont{fzhupoj}{FZHPJW.TTF}
\newcommand{\fzhupoj}{\CJKfamily{fzhupoj}}
\setCJKfamilyfont{fztiejinlishuj}{FZTJLSJW.TTF}
\newcommand{\fztiejinlishuj}{\CJKfamily{fztiejinlishuj}}
\setCJKfamilyfont{fzpangwaj}{FZPWJW.TTF}
\newcommand{\fzpangwaj}{\CJKfamily{fzpangwaj}}
\setCJKfamilyfont{fzyiheij}{FZYHJW.TTF}
\newcommand{\fzyiheij}{\CJKfamily{fzyiheij}}
\setCJKfamilyfont{fzshoujinshuj}{FZSJSJW.TTF}
\newcommand{\fzshoujinshuj}{\CJKfamily{fzshoujinshuj}}
\setCJKfamilyfont{fzshuti}{fzstk.TTF}
\newcommand{\fzshuti}{\CJKfamily{fzshuti}}
\setCJKfamilyfont{fzmeiheij}{FZMHJW.TTF}
\newcommand{\fzmeiheij}{\CJKfamily{fzmeiheij}}
\setCJKfamilyfont{fzxishanhuj}{FZXSHJW.TTF}
\newcommand{\fzxishanhuj}{\CJKfamily{fzxishanhuj}}
\setCJKfamilyfont{fzsongyij}{FZSYJW.TTF}
\newcommand{\fzsongyij}{\CJKfamily{fzsongyij}}
\setCJKfamilyfont{fzmiaomingti}{FZMWFont.TTF}
\newcommand{\fzmiaomingti}{\CJKfamily{fzmiaomingti}}
\setCJKfamilyfont{fzxinshutij}{FZNSTJW.TTF}
\newcommand{\fzxinshutij}{\CJKfamily{fzxinshutij}}
\setCJKfamilyfont{fzxiqianj}{FZXQJW.TTF}
\newcommand{\fzxiqianj}{\CJKfamily{fzxiqianj}}
\setCJKfamilyfont{fzzhanbiheij}{FZZBHJW.TTF}
\newcommand{\fzzhanbiheij}{\CJKfamily{fzzhanbiheij}}
\setCJKfamilyfont{fzbaosongj}{FZBSJW.TTF}
\newcommand{\fzbaosongj}{\CJKfamily{fzbaosongj}}
\setCJKfamilyfont{fzxianglij}{FZXIANGLJW.TTF}
\newcommand{\fzxianglij}{\CJKfamily{fzxianglij}}
\setCJKfamilyfont{fzchuqianj}{FZCQJW.TTF}
\newcommand{\fzchuqianj}{\CJKfamily{fzchuqianj}}
\setCJKfamilyfont{fzyaotij}{FZYTJW.TTF}
\newcommand{\fzyaotij}{\CJKfamily{fzyaotij}}
\setCJKfamilyfont{fzchuyuanj}{FZY4JW.TTF}
\newcommand{\fzchuyuanj}{\CJKfamily{fzchuyuanj}}
\setCJKfamilyfont{fzkatongf}{FZKATFW.TTF}
\newcommand{\fzkatongf}{\CJKfamily{fzkatongf}}
\setCJKfamilyfont{fzhepingj}{FZPHTJW.TTF}
\newcommand{\fzhepingj}{\CJKfamily{fzhepingj}}
\setCJKfamilyfont{fzshuizhuj}{FZSZJW.TTF}
\newcommand{\fzshuizhuj}{\CJKfamily{fzshuizhuj}}
\setCJKfamilyfont{fzzhiyij}{FZZHYJW.TTF}
\newcommand{\fzzhiyij}{\CJKfamily{fzzhiyij}}

\fi

%\providecommand{\CJKnumber}[1]{\ifcase#1\or{一}\or{二}\or{三}\or{四}\or{五}\or{六}\or{七}\or{八}\or{九}\or{十}\fi}
\@ifundefined{CJKnumber}
  {\def\CJKnumber#1{\ifcase#1\or
                    一\or二\or三\or四\or五\or
                    六\or七\or八\or九\or十\or十一\or十二\or十三\or十四\or十五\fi}}{}

\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\ifmyxecjk
\RequirePackage[BoldFont, SlantFont, CJKnumber]{xeCJK} % xeCJK package
%\punctstyle{kaiming}
\setmainfont[Mapping=tex-text]{Times New Roman}%\rmfamily 使用的字体,默认英文和数字的字体。
\XeTeXlinebreaklocale "zh" %采用中文断行方式
\XeTeXlinebreakskip = 0pt plus 1pt %字元间可加入0pt~1pt 的弹性间距，这样才能排出左右对齐的段落。
\RequirePackage{CJKnumb}
\setsansfont{Arial}
\setmonofont{Courier New}

\setCJKmainfont{SimSun}%{FangSong_GB2312}%{SimSun}
\setCJKsansfont{SimHei}
\setCJKmonofont{KaiTi_GB2312}

\setCJKfamilyfont{song}{SimSun}
\setCJKfamilyfont{hei}{SimHei}
\setCJKfamilyfont{kai}{KaiTi_GB2312}
\setCJKfamilyfont{fang}{FangSong_GB2312}
\setCJKfamilyfont{you}{YouYuan}
\setCJKfamilyfont{li}{LiSu}
\newcommand{\songti}{\CJKfamily{song}}
\newcommand{\heiti}{\CJKfamily{hei}}
\newcommand{\kaiti}{\CJKfamily{kai}}
\newcommand{\fangsong}{\CJKfamily{fang}}
\newcommand{\youyuan}{\CJKfamily{you}}
\newcommand{\lishu}{\CJKfamily{li}}%隶书

%%huawenziti
\setCJKfamilyfont{hwxihei}{STXihei}%华文细黑
\newcommand{\hwxihei}{\CJKfamily{hwxihei}}
\setCJKfamilyfont{hwxinwei}{STXinwei}%华文新魏
\newcommand{\hwxinwei}{\CJKfamily{hwxinwei}}
\setCJKfamilyfont{hwfangsong}{STFangsong}%华文仿宋
\newcommand{\hwfangsong}{\CJKfamily{hwfangsong}}
\setCJKfamilyfont{hwxingkai}{STXingkai}%华文行楷,
\newcommand{\hwxingkai}{\CJKfamily{hwxingkai}}
\setCJKfamilyfont{hwzhongsong}{STZhongsong}%华文中宋
\newcommand{\hwzhongsong}{\CJKfamily{hwzhongsong}}
\setCJKfamilyfont{hwhupo}{STHupo}%华文琥珀,
\newcommand{\hwhupo}{\CJKfamily{hwhupo}}
\setCJKfamilyfont{hwkaiti}{STKaiti}%华文楷体
\newcommand{\hwkaiti}{\CJKfamily{hwkaiti}}
\setCJKfamilyfont{hwcaiyun}{STCaiyun}%华文彩云
\newcommand{\hwcaiyun}{\CJKfamily{hwcaiyun}}
\setCJKfamilyfont{hwsongti}{STSong}%华文宋体
\newcommand{\hwsongti}{\CJKfamily{hwsongti}}
\setCJKfamilyfont{hwlishu}{STLiti}%华文隶书
\newcommand{\hwlishu}{\CJKfamily{hwlishu}}

%adobefont
\setCJKfamilyfont{adobefs}{Adobe Fangsong Std}
\newcommand{\adobefs}{\CJKfamily{adobefs}}
\setCJKfamilyfont{adobesong}{Adobe Song Std}
\newcommand{\adobesong}{\CJKfamily{adobesong}}
\setCJKfamilyfont{adobefbheiti}{Adobe Fan Heiti Std}
\newcommand{\adobefbheiti}{\CJKfamily{adobefbheiti}}
\setCJKfamilyfont{adobekaiti}{Adobe Kaiti Std}
\newcommand{\adobefkaiti}{\CJKfamily{adobefkaiti}}
\setCJKfamilyfont{adobemingti}{Adobe Ming Std}
\newcommand{\adobefmingti}{\CJKfamily{adobefmingti}}
\setCJKfamilyfont{adobeheiti}{Adobe Heiti Std}
\newcommand{\adobefheiti}{\CJKfamily{adobefheiti}}

%cwtexfont
\setCJKfamilyfont{cwheiti}{cwTeXHeiBold}
\newcommand{\cwheiti}{\CJKfamily{cwheiti}}
\setCJKfamilyfont{cwmingti}{cwTeXMing}
\newcommand{\cwmingti}{\CJKfamily{cwmingti}}%,cwTeX明體
\setCJKfamilyfont{cwkaiti}{cwTeXKai}
\newcommand{\cwkaiti}{\CJKfamily{cwkaiti}}%,cwTeX楷書
\setCJKfamilyfont{cwfs}{cwTeXFangSong}
\newcommand{\cwfs}{\CJKfamily{cwfs}}%,cwTeX仿宋體
\setCJKfamilyfont{cwyuanti}{cwTeXYen}
\newcommand{\cwyuanti}{\CJKfamily{cwyuanti}}%,cwTeX圓體

%fangzhengziti
\setCJKfamilyfont{fzsong}{Simsun (Founder Extended)}%方正宋体超大字符集   fzsong
\newcommand{\fzsong}{\CJKfamily{fzsong}}
\setCJKfamilyfont{fzqitij}{方正启体简体}
\newcommand{\fzqitij}{\CJKfamily{fzqitij}}
\setCJKfamilyfont{fzdaheij}{方正大黑简体}
\newcommand{\fzdaheij}{\CJKfamily{fzdaheij}}
\setCJKfamilyfont{fztechughj}{方正特粗光辉简体}
\newcommand{\fztechughj}{\CJKfamily{fztechughj}}
\setCJKfamilyfont{fzzhengsongsanj}{方正宋三简体}
\newcommand{\fzzhengsongsanj}{\CJKfamily{fzzhengsongsanj}}
\setCJKfamilyfont{fzxbs}{方正小标宋简体}
\newcommand{\fzxbs}{\CJKfamily{fzxbs}}
\setCJKfamilyfont{fzshaoerj}{方正少儿简体}
\newcommand{\fzshaoerj}{\CJKfamily{fzshaoerj}}
\setCJKfamilyfont{fzzhengkaij}{方正行楷简体}
\newcommand{\fzzhengkaij}{\CJKfamily{fzzhengkaij}}
\setCJKfamilyfont{fzzongyij}{方正综艺简体}
\newcommand{\fzzongyij}{\CJKfamily{fzzongyij}}
\setCJKfamilyfont{fzyinbixingshuj}{方正硬笔行书简体}
\newcommand{\fzyinbixingshuj}{\CJKfamily{fzyinbixingshuj}}
\setCJKfamilyfont{fzsuxinshiliukaij}{方正苏新诗柳楷简体}
\newcommand{\fzsuxinshiliukaij}{\CJKfamily{fzsuxinshiliukaij}}
\setCJKfamilyfont{fzshuiheij}{方正水黑简体}
\newcommand{\fzshuiheij}{\CJKfamily{fzshuiheij}}
\setCJKfamilyfont{fzxiyuanj}{方正细圆简体}
\newcommand{\fzxiyuanj}{\CJKfamily{fzxiyuanj}}
\setCJKfamilyfont{fzyaoti}{FZYaoTi}
\newcommand{\fzyaoti}{\CJKfamily{fzyaoti}}
\setCJKfamilyfont{fzxidengxianj}{方正细等线简体}
\newcommand{\fzxidengxianj}{\CJKfamily{fzxidengxianj}}
\setCJKfamilyfont{fzxiheiyij}{方正细黑一简体}
\newcommand{\fzxiheiyij}{\CJKfamily{fzxiheiyij}}
\setCJKfamilyfont{fzgulij}{方正古隶简体}
\newcommand{\fzgulij}{\CJKfamily{fzgulij}}
\setCJKfamilyfont{fzpangtouyuj}{方正胖头鱼简体}
\newcommand{\fzpangtouyuj}{\CJKfamily{fzpangtouyuj}}
\setCJKfamilyfont{fzyouxianj}{方正幼线简体}
\newcommand{\fzyouxianj}{\CJKfamily{fzyouxianj}}
\setCJKfamilyfont{fzshutij}{方正舒体简体}
\newcommand{\fzheipingpf}{\CJKfamily{fzheipingpf}}
\setCJKfamilyfont{fzyinbikaishuj}{方正硬笔楷书简体}
\newcommand{\fzyinbikaishuj}{\CJKfamily{fzyinbikaishuj}}
\setCJKfamilyfont{fzkangtij}{方正康体简体}
\newcommand{\fzkangtij}{\CJKfamily{fzkangtij}}
\setCJKfamilyfont{fzhupoj}{方正琥珀简体}
\newcommand{\fzhupoj}{\CJKfamily{fzhupoj}}
\setCJKfamilyfont{fztiejinlishuj}{方正铁筋隶书简体}
\newcommand{\fztiejinlishuj}{\CJKfamily{fztiejinlishuj}}
\setCJKfamilyfont{fzpangwaj}{方正胖娃简体}
\newcommand{\fzpangwaj}{\CJKfamily{fzpangwaj}}
\setCJKfamilyfont{fzyiheij}{方正艺黑简体}
\newcommand{\fzyiheij}{\CJKfamily{fzyiheij}}
\setCJKfamilyfont{fzshoujinshuj}{方正瘦金书简体}
\newcommand{\fzshoujinshuj}{\CJKfamily{fzshoujinshuj}}
\setCJKfamilyfont{fzkaitij}{方正楷体简体}
\newcommand{\fzkaitij}{\CJKfamily{fzkaitij}}
\setCJKfamilyfont{fzshuti}{方正舒体}%,FZShuTi
\newcommand{\fzshuti}{\CJKfamily{fzshuti}}
\setCJKfamilyfont{fzmeiheij}{方正美黑简体}
\newcommand{\fzmeiheij}{\CJKfamily{fzmeiheij}}
\setCJKfamilyfont{fzxiaozhuanti}{方正小篆体}
\newcommand{\fzxiaozhuanti}{\CJKfamily{fzxiaozhuanti}}
\setCJKfamilyfont{fzxishanhuj}{方正细珊瑚简体}
\newcommand{\fzxishanhuj}{\CJKfamily{fzxishanhuj}}
\setCJKfamilyfont{fzsongyij}{方正宋一简体}
\newcommand{\fzsongyij}{\CJKfamily{fzsongyij}}
\setCJKfamilyfont{fzmiaomingti}{方正喵呜体}
\newcommand{\fzmiaomingti}{\CJKfamily{fzmiaomingti}}
\setCJKfamilyfont{fzsongheij}{方正宋黑简体}
\newcommand{\fzsongheij}{\CJKfamily{fzsongheij}}
\setCJKfamilyfont{fzxinshutij}{方正新舒体简体}
\newcommand{\fzxinshutij}{\CJKfamily{fzxinshutij}}
\setCJKfamilyfont{fzxiqianj}{方正细倩简体}
\newcommand{\fzxiqianj}{\CJKfamily{fzxiqianj}}
\setCJKfamilyfont{fzdabiaosongj}{方正大标宋简体}
\newcommand{\fzdabiaosongj}{\CJKfamily{fzdabiaosongj}}
\setCJKfamilyfont{fzzhanbiheij}{方正毡笔黑简体}
\newcommand{\fzzhanbiheij}{\CJKfamily{fzzhanbiheij}}
\setCJKfamilyfont{fzbaosongj}{方正报宋简体}
\newcommand{\fzbaosongj}{\CJKfamily{fzbaosongj}}
\setCJKfamilyfont{fzxianglij}{方正祥隶简体}
\newcommand{\fzxianglij}{\CJKfamily{fzxianglij}}
\setCJKfamilyfont{fzchusongj}{方正粗宋简体}
\newcommand{\fzchusongj}{\CJKfamily{fzchusongj}}
\setCJKfamilyfont{fzchuqianj}{方正粗倩简体}
\newcommand{\fzchuqianj}{\CJKfamily{fzchuqianj}}
\setCJKfamilyfont{fzyaotij}{方正姚体简体}
\newcommand{\fzyaotij}{\CJKfamily{fzyaotij}}
\setCJKfamilyfont{fzchuyuanj}{方正粗圆简体}
\newcommand{\fzchuyuanj}{\CJKfamily{fzchuyuanj}}
\setCJKfamilyfont{fzcaiyunj}{方正彩云简体}
\newcommand{\fzcaiyunj}{\CJKfamily{fzcaiyunj}}
\setCJKfamilyfont{fzkatongf}{方正卡通繁体}
\newcommand{\fzkatongf}{\CJKfamily{fzkatongf}}
\setCJKfamilyfont{fzhepingj}{方正平和简体}
\newcommand{\fzhepingj}{\CJKfamily{fzhepingj}}
\setCJKfamilyfont{fzshuizhuj}{方正水柱简体}
\newcommand{\fzshuizhuj}{\CJKfamily{fzshuizhuj}}
\setCJKfamilyfont{fzzhiyij}{方正稚艺简体}
\newcommand{\fzzhiyij}{\CJKfamily{fzzhiyij}}
\setCJKfamilyfont{fzxinbaosongj}{方正新报宋简体}
\newcommand{\fzxinbaosongj}{\CJKfamily{fzxinbaosongj}}
\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%直排汉字版本%%%
\ifadobefontv
\RequirePackage[BoldFont, SlantFont, CJKnumber]{xeCJK} % xeCJK package
\RequirePackage{CJKnumb}
%\punctstyle{kaiming}
%\setmainfont[Mapping=tex-text]{Times New Roman}%\rmfamily 使用的字体,默认英文和数字的字体。
\XeTeXlinebreaklocale "zh" %采用中文断行方式
\XeTeXlinebreakskip = 0pt plus 1pt %字元间可加入0pt~1pt 的弹性间距，这样才能排出左右对齐的段落。
\RequirePackage{zhspacing}
%\XeTeXinputencoding "cp936"
%\zhspacing
\RequirePackage{zhulem}
\RequirePackage{atbegshi}
\AtBeginShipout{%
\global\setbox\AtBeginShipoutBox\vbox{%
\special{pdf:put@thispage<</Rotate 180>>}%
\box\AtBeginShipoutBox
}%
}
%%%or other style%%
%\iffalse
%\RequirePackage{everyshi}
%\makeatletter
%\EveryShipout{
%        \global\setbox\@cclv\vbox{%
%          \special{pdf: put @thispage << /Rotate 90 >>}%
%          \box\@cclv
%        }%
%}%
%\makeatother
%\fi
\setCJKmainfont[RawFeature={vertical}]{AdobeSongStd-Light}%{FangSong_GB2312}%{SimSun}
\setCJKsansfont[RawFeature={vertical}]{AdobeHeitiStd-Regular}
\setCJKmonofont[RawFeature={vertical}]{AdobeKaitiStd-Regular}

\setCJKfamilyfont{songv}[RawFeature={vertical}]{AdobeSongStd-Light}
\setCJKfamilyfont{fsv}[RawFeature={vertical}]{AdobeFangSongStd-Regular}
\setCJKfamilyfont{heiv}[RawFeature={vertical}]{AdobeHeitiStd-Regular}
\setCJKfamilyfont{kaiv}[RawFeature={vertical}]{AdobeKaitiStd-Regular}%
\setCJKfamilyfont{fheiv}[RawFeature={vertical}]{AdobeFanHeitiStd-Bold}
\setCJKfamilyfont{mingv}[RawFeature={vertical}]{AdobeMingStd-Light}
\setCJKfamilyfont{yungV}[RawFeature={vertical}]{AdobeMyungjoStd-Medium}

\newcommand{\songti}{\CJKfamily{songv}} % 宋体
\newcommand{\heiti}{\CJKfamily{heiv}}   % 黑体
\newcommand{\kaiti}{\CJKfamily{kaiv}}  % 楷书
\newcommand{\fangsong}{\CJKfamily{fsv}} % 仿宋
\newcommand{\fanghei}{\CJKfamily{fheiv}} % 仿宋黑体
\newcommand{\mingti}{\CJKfamily{mingv}} % 仿宋黑体
\newcommand{\adobezw}{\CJKfamily{yungv}} %adobe中文

\makeatother
%\setgezhuraise{-5pt}
\def\myfeat{vertical:+vert:+vhal}
\def\mysep{.}
%\sepskip=0.1em plus 0.4em minus 0.1em\relax
\newfontfamily\adobesong[RawFeature={\myfeat}]{[AdobeSongStd-Light.otf]}
\newfontfamily\hkstdkai[RawFeature={\myfeat}]{DFPHKStdKai-B5}
\let\zhfont\hkstdkai
\let\zhpunctfont\adobesong
\halthalfskipscheme
\def\skipzhlineendfullstop{\hskip -.2em}
\def\skipnegzhlineendfullstop{\hskip .2em}
\iffalse
\krap\qit\piengx\teng\muh\kix\krang\sin\njim\kjyix
\cix\thriux\jin\mraux\zjin\zsix\ngox\myoih\sjin
\fi
\makeatletter
%%%%%%%%%开本-版心-边距设置%%%%%%%%%%%%%%%%
\setlength{\hoffset}{0mm}%
\setlength{\voffset}{0mm}
%\setlength{\textwidth}{470pt}
%\setlength{\textheight}{560pt}
\setlength{\marginparwidth}{0pt}
\setlength{\oddsidemargin}{10pt}
\setlength{\evensidemargin}{10pt}
%\setlength{\topmargin}{-26pt}
%\setlength{\headsep}{63pt}
\setlength{\parskip}{0pt}

%字间距和字体的位置设置，具体参数，根据选用字体调整
        \let\hCJKsymbol\CJKsymbol
        \def\vCJKsymbol#1{\hskip 2pt plus 0pt minus 0pt\lower 0.1em%
        \vbox to 1em{\vskip 0em\hbox{\hCJKsymbol{#1}}}}
        \let\CJKsymbol\vCJKsymbol
%设置标点位置在字的右下角，而不占任何位置，具体参数，根据选用字体调整
%\iffalse
        \def\vCJKpunctsymbol#1{\hskip -1em plus 0pt minus 0pt\lower 0em%
        \vbox to 0em{\vskip -1.8em\hbox{\hCJKsymbol{#1}}}}
        \let\CJKpunctsymbol\vCJKpunctsymbol
%\fi
%pdf的横向输出控制
%\RequirePackage{pdflscape}%\begin{landscape}\end{landscape}
%表格和微表格宏包，用于双行割注
\newcommand{\minitab}[2][l]{\begin{tabular}{#1}#2\end{tabular}}
%书名目录等设置，用于书耳
%\def\booktitle{任傑居士文集~~~第一部}
%\def\leftmark{第一冊~~~法相集釋}
 \renewcommand{\contentsname}{\bf{目\qquad 錄}}
%%% 竖排古文中的标点优化，让标点不占位置，
%%%逗号句号顿号问号冒号惊叹号等可以不使用优化，
%%%不过如果不优化，标点有点儿太大，显得很蠢
\iffalse
\def\QuaF{\makebox[0pt][r]{\raisebox{0.4em}{\rotatebox{-90}{\large {『}\rule{0em}{0.9em}}}}}%前双引号
\def\QuaB{\makebox[0pt][r]{\raisebox{-0.2em}{\rotatebox{-90}{\large {』}\rule{0em}{1em}}}}}%后双引号
\def\QuaFD{\makebox[0pt][r]{\raisebox{0.35em}{\rotatebox{-90}{\large {「}\rule{0em}{0.9em}}}}}%前单引号
\def\QuaBD{\makebox[0pt][r]{\raisebox{-0.2em}{\rotatebox{-90}{\large {」}\rule{0em}{1em}}}}}
\def\JuDou#1{\makebox[0pt][l]{\raisebox{0.4em}{\large {#1}}}}%句号逗号顿号等
\def\JuDous#1{\makebox[0pt][l]{\hskip -0.2em\raisebox{-0.4em}{\large {#1}}}}%双行小字的左侧行句号逗号顿号等
\def\HanT{\makebox[0pt][l]{\raisebox{0.4em}{\large {！}}}}%惊叹号
\def\QuestM#1{\makebox[0pt][r]{\raisebox{0.4em}{\normalsize {#1}}}}%问好
\fi
%%%这个是自己做了图，没有使用已有宏包，主要为了效果好看和断行准确
%\def\cB{\makebox[0pt][r]{\includegraphics[height=22pt]{wave1.png}}}%书名号
%\def\cP{\makebox[0pt][r]{\includegraphics[height=22pt]{topbar1.png}}}%人名地名号
%%%双行小字短割注
\def\vGZ#1#2{\raisebox{0.35em}{\hskip -0.15em\scalebox{1}[0.35]{\minitab{\fontsize{20pt}{10pt}\selectfont#1}#2}}\hskip -0.15em}
%小字夹住，单行，非割注形式，长方形字体
\def\vSC#1{\mbox{\raisebox{0.4em}{\scalebox{1}[0.5]{#1}}}}
%小字旁注，长方形字体
\def\cCM#1{\makebox[0pt][l]{\raisebox{1.02em}{\scalebox{1}[0.5]{#1}}}}
%小字旁注，正方形小字
\def\Szhu#1{\makebox[0pt][l]{\raisebox{1.02em}{\scalebox{0.5}[0.5]{#1}}}}
%小标题
\def\Xbt#1{\raisebox{0.25em}{\scalebox{1}[0.75]{#1}}}
%小小标题
\def\XXbt#1{\raisebox{0.45em}{\scalebox{1}[0.5]{#1}}}
%页眉页脚的包和设置
%\RequirePackage{fancyhdr}
%        \pagestyle{fancy}
%        \fancyhf{} %清空页眉页
%这个有问题，没找到显示中文数字页码的办法
%\fancyhead[CO]{\fontsize{20pt}{20pt}\selectfont\rotatebox{180}{\thepage}}
%\fancyhead[CE]{\fontsize{20pt}{20pt}\selectfont\rotatebox{180}{\thepage}}
%利用页眉页脚制作书耳，如果使用去掉注释即可
%\fancyfoot[RO]{\makebox[0pt][l]{\hphantom{MM}\rotatebox[origin=r]{90}{\makebox[0pt][l]{\hphantom{mm}{\large\CJKfamily{KePan}\booktitle}}}}}
%\fancyfoot[LE]{\makebox[0pt][r]{\rotatebox[origin=l]{90}{\makebox[0pt][l]{\hphantom{mm}{\large\CJKfamily{KePan}\leftmark}}}\hphantom{MMl}}}
%去掉页眉线
%\renewcommand{\headrulewidth}{0pt}
\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Font size
\iftexsize
\newcommand{\chuhao}{\fontsize{42pt}{46pt}\selectfont}
\newcommand{\xiaochuhao}{\fontsize{36pt}{40pt}\selectfont}
\newcommand{\yichu}{\fontsize{32pt}{36pt}\selectfont}
\newcommand{\yihao}{\fontsize{28pt}{32pt}\selectfont}
\newcommand{\erhao}{\fontsize{21pt}{24pt}\selectfont}
\newcommand{\xiaoerhao}{\fontsize{18pt}{20}\selectfont}
\newcommand{\sanhao}{\fontsize{15.75pt}{18pt}\selectfont}
\newcommand{\mysanhao}{\fontsize{17pt}{18pt}\selectfont}
%\newcommand{\xiaosanhao}{\fontsize{15bp}{18pt plus .3pt minus .2pt}\selectfont}
\newcommand{\xiaosanhao}{\fontsize{15pt}{22.5pt}\selectfont}%1.5
\newcommand{\sihao}{\fontsize{14pt}{16pt}\selectfont}
\newcommand{\xiaosihao}{\fontsize{12pt}{14pt}\selectfont}
\newcommand{\wuhao}{\fontsize{10.5pt}{13pt}\selectfont}
\newcommand{\xiaowuhao}{\fontsize{9pt}{11pt}\selectfont}
\newcommand{\liuhao}{\fontsize{7.5pt}{9pt}\selectfont}
\newcommand{\xiaoliuhao}{\fontsize{6.5pt}{7.5pt}\selectfont}
\newcommand{\qihao}{\fontsize{5.5pt}{6.5pt}\selectfont}
\newcommand{\bahao}{\fontsize{5.35pt}{6.4pt}\selectfont}
\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Font size
\ifmsize
\newcommand{\chuhao}{\fontsize{42pt}{46pt}\selectfont}
\newcommand{\xiaochuhao}{\fontsize{36pt}{40pt}\selectfont}
\newcommand{\yichu}{\fontsize{32pt}{36pt}\selectfont}
\newcommand{\yihao}{\fontsize{25.98pt}{26pt}\selectfont}
\newcommand{\xiaoyihao}{\fontsize{24pt}{25pt}\selectfont}
\newcommand{\erhao}{\fontsize{22.02pt}{23pt}\selectfont}
\newcommand{\xiaoerhao}{\fontsize{18pt}{20}\selectfont}
\newcommand{\sanhao}{\fontsize{16.02pt}{18pt}\selectfont}
\newcommand{\xiaosanhao}{\fontsize{15pt}{16pt}\selectfont}
\newcommand{\sihao}{\fontsize{13.98pt}{15pt}\selectfont}
\newcommand{\xiaosihao}{\fontsize{12pt}{14pt}\selectfont}
\newcommand{\wuhao}{\fontsize{10.5pt}{11pt}\selectfont}
\newcommand{\xiaowuhao}{\fontsize{9pt}{11pt}\selectfont}
\newcommand{\liuhao}{\fontsize{7.5pt}{8pt}\selectfont}
\newcommand{\xiaoliuhao}{\fontsize{6.48pt}{7pt}\selectfont}
\newcommand{\qihao}{\fontsize{5.52pt}{6.5pt}\selectfont}
\newcommand{\bahao}{\fontsize{4.98pt}{6pt}\selectfont}
\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\toctitlefont}{\heiti\xiaoerhao}        % “目录”字样的字体
\newcommand{\tocchapterfont}{\heiti\xiaosihao} % 目录上第X章的字体
\newcommand{\tocsectionfont}{\normalsize}         % 目录上X.Y节的字体
\newcommand{\tocsubsectionfont}{\normalsize}      % 目录上X.Y.Z小节的字体
\newcommand{\tocsubsubsectionfont}{\normalsize}      % 目录上X.Y.Z小节的字体
\newcommand{\textchapterfont}{\centering\heiti\xiaoerhao} % 正文上第X章的字体
\newcommand{\textsectionfont}{\heiti\xiaosanhao}       % 正文上X.Y节的字体
\newcommand{\textsubsectionfont}{\heiti\sihao}     % 正文上X.Y.Z小节的字体
\newcommand{\textsubsubsectionfont}{\heiti\xiaosihao} % 正文上X.Y.Z.K小节的字体
\newcommand{\footnotefont}{\songti\xiaowuhao\normalfont}  % 脚注字体
\newcommand{\ftcaptionfont}{\kaiti\wuhao\normalfont}      % 图表标题的字体
\newcommand{\reftitlefont}{\heiti\xiaoerhao}      % “参考文献”字样的字体
\newcommand{\refbodyfont}{\songti\wuhao\normalfont}          % 参考文献字体
\newcommand{\thanktitlefont}{\heiti\sanhao}    % “致谢”字样的字体
\newcommand{\appendixtitlefont}{\heiti\sanhao} % “附录”字样的字体
%%%%%%%%%%%%%%%%%%%
\newcommand{\absnamecn}{\songti\xiaosihao\bfseries}         % 中文“摘要”字样的字体
\newcommand{\abskeycn}{\songti\xiaosihao\bfseries}       % 中文摘要“关键字”字样的字体
\newcommand{\abskeyscn}{\songti\xiaosihao} % 中文摘要关键字的字体
\newcommand{\absnameen}{\bfseries\xiaosihao} % 英文``Abstract''字样的字体
\newcommand{\abskeyen}{\bfseries\xiaosihao}  % 英文``KEY WORDS''字样的字体
\newcommand{\abskeysen}{\xiaosihao} % 英文关键字的字体
\newcommand{\headfont}{\songti\wuhao}% 页眉字体
%%%%%%%%%%%%%%%%%%%
\newcommand{\cndash}{\rule{0.0em}{0pt}\rule[0.35em]{1.4em}{0.05em}\rule{0.2em}{0pt}} % 中文破折号,added by Quansheng
% My fonts for Scut course paper
%\renewcommand{\normalsize}{\xiaosihao\songti} % Normal font size 小四号宋体
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\RequirePackage{caption} % 定义图的标题格式：居中. 使用caption3.0
\DeclareCaptionFont{capFont}{\ftcaptionfont} % 表格名及图名
\DeclareCaptionLabelSeparator{twospace}{~~}
\captionsetup{
  labelsep=twospace,% 去掉图标签后的冒号
  font={capFont},%
  figurename=图,%
  tablename=表,%
  listfigurename=插图目录,%
  listtablename=表格目录}
%%%%%%%%%%%%%%%%%%%%%%%%%
\renewcommand{\theequation}{\arabic{section}-\arabic{equation}}
\renewcommand{\thetable}{\arabic{section}-\arabic{table}}
\renewcommand{\thefigure}{\arabic{section}-\arabic{figure}}
\renewcommand{\thefootnote}{注\arabic{footnote}} \setcounter{footnote}{0}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
%\addtocounter{enumi}{1}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
\renewcommand\fps@figure{htbp} % 设置图浮动的默认参数
\renewcommand\fps@table{htbp}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55
\renewcommand{\textfraction}{0.07}
\renewcommand{\topfraction}{0.9}
\renewcommand{\bottomfraction}{0.8}
\renewcommand{\floatpagefraction}{0.85}
%%%%%%%%%参考文献设置二
\RequirePackage[numbers,sort&compress]{natbib}
\RequirePackage{hypernat}
\let\ncite\cite
\renewcommand\cite[2][]{\textsuperscript{\ncite[#1]{#2}}}
\newcommand\scite[2][]{\textsuperscript{\ncite[#1]{#2}}}
%%%%%%%%%%%%%%%%%%%%%%%%设置bibistyle
\let\orig@bibliography=\bibliography
\renewcommand{\bibliography}[1]{
        \clearpage%使参考文献使用seunolabel页面样式
        \refbodyfont
        \orig@bibliography{#1}
        \normalsize
}
\RequirePackage[nottoc]{tocbibind}%将参考文献、索引、表格目录和图形
\renewcommand{\bibname}{参考文献}
%%%%%%%%%%%%%%%%%%%%%%%%%%
% 设置目录
%%%%%%%%%%%%%%%%%
\RequirePackage{titletoc} 
\renewcommand\contentsname{\centerline{\toctitlefont{目\quad{}录}}}
%\titlecontents{chapter}[0ex]{\tocchapterfont}{%
%    第\CJKnumber{\thecontentslabel}章\quad{}}{}{%
%    \hspace{.5em}\titlerule*[5pt]{$\cdot$}\contentspage}%
\titlecontents{section}[1em]{\tocsectionfont}{%
    \S\thecontentslabel\quad{}}{}{%
    \hspace{.5em}\titlerule*[5pt]{$\cdot$}\contentspage}%
\titlecontents{subsection}[2em]{\tocsubsectionfont}{%
    \thecontentslabel\quad{}}{}{%
    \hspace{.5em}\titlerule*[5pt]{$\cdot$}\contentspage}%
\titlecontents{subsubsection}[3em]{\tocsubsubsectionfont}{%
    \thecontentslabel\quad{}}{}{%
    \hspace{.5em}\titlerule*[5pt]{$\cdot$}\contentspage}%
%%%%%%%%%%%%%%
% 设定章节深度和目录深度
\setcounter{secnumdepth}{4}
\setcounter{tocdepth}{3}
%%%%%%%%%%%%
% Text style
\RequirePackage[pagestyles, rm]{titlesec}%调用titlesec涵盖fancyhdr的功能
\titleformat{\section}[hang]{\textsectionfont}{\thesection}{1em}{}
\titleformat{\subsection}[hang]{\textsubsectionfont}{\thesubsection}{1em}{}
\titleformat{\subsubsection}[hang]{\textsubsectionfont}{\thesubsubsection}{1ex}{}% 小四黑体居左

\setlength{\parskip}{0ex}% 正文段前段后距：无空行
\titlespacing{\section}{0pt}{4pt}{4pt}  % 标题间距
\titlespacing{\subsection}{0pt}{4pt}{0pt} 
\titlespacing{\subsubsection}{0pt}{6pt}{6pt} 

\newcommand{\linespacing}[1]{\linespread{#1}\selectfont}% 行距命令

%\sethead[ even-left ][ even-center ][ even-right ]    { odd-left }{ odd-center }{ odd-right }
\newpagestyle{revtitlestyle}{
  \sethead[][{\headfont{}\thesissubject}][] % 页眉偶数页，五号字体，居中
  {}{{\headfont{}\thesection\quad\sectiontitle}}{} % 页眉奇数页，五号字体，居中
  \setfoot{}{{\headfont{}\wuhao \thepage}}{}%页码五号宋体居中
  \headrule%上横线
  \setheadrule{1.5pt}%设置横线粗细
}
\newpagestyle{revtitlenolabstyle}{
  \sethead[][{\headfont{}\thesissubject}][] % 页眉偶数页，五号字体，居中
  {}{{\headfont{}\sectiontitle}}{} % 页眉奇数页，五号字体，居中
  \setfoot{}{{\headfont{}\wuhao \thepage}}{}%页码五号宋体居中
  \headrule%上横线
  \setheadrule{1.5pt}%设置横线粗细
}

\renewpagestyle{plain}{
  \setfoot{}{{\wuhao \thepage}}{}
}
%%%%%%
\newcommand{\myclearpage}{%
  \ifonepage
    \clearpage
  \else
    \cleardoublepage
  \fi
}
%%%%%%%%%%%%%%%%%%%%%
%定义表格的竖立居中
\newcommand{\PreserveBackslash}[1]{\let\temp=\\#1\let\\=\temp}
\newcolumntype{C}[1]{>{\PreserveBackslash\centering}m{#1}}
\newcolumntype{R}[1]{>{\PreserveBackslash\raggedleft}m{#1}}
\newcolumntype{L}[1]{>{\PreserveBackslash\raggedright}m{#1}}
%%%%%%%%%%%%%%
\newcounter{enumv} %自定义新计数器
\newcounter{smsnum} %自定义新计数器
\renewcommand{\theenumi} {\arabic{enumi}.}%1.
\renewcommand{\labelenumi}{\theenumi}

\renewcommand{\theenumii}{\arabic{enumi}.\arabic{enumii}}  %1.1
\renewcommand{\labelenumii}{\theenumii}

\renewcommand{\theenumiii}{\arabic{enumiii})} %1)
\renewcommand{\labelenumiii}{\theenumiii}

\renewcommand{\theenumiv}{\textcircled{\small\arabic{enumiv}}}  %圈1
\renewcommand{\labelenumiv}{\theenumiv}

\newcommand{\labelenumv}{\alph{enumv}.} %a.

\newenvironment{msmlist}
{\addtocounter{smsnum}{1}%%%%%定义新环境
\begin{list}{\csname labelenum\roman{smsnum}\endcsname}%{\csname labelenum\roman{smsnum}}%%标签格式
    {
     \usecounter{enum\roman{smsnum}}
     }
}
{\addtocounter{smsnum}{-1} \end{list}}%
%%%%%%%%%%%%%%%%%%------------------
\newcommand{\chntoday}{\the\year~年~\the\month~月~\the\day~日}
\newcommand{\CHNtoday}{\CJKdigits{\the\year}~年~\CJKnumber{\the\month}~月~\CJKnumber{\the\day}~日}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\blackpage}{\newpage\hspace*{2em}\newpage}%增加一空白页
\newcommand{\gdhsfj}[1]{\parindent=0pt \textcolor{black}{\xiaoerhao\fzxbs #1}}
\newcommand{\dk}[1]{\par{\parindent=0pt#1}}
\newcommand{\md}[1]{\par\hspace{7cm}\begin{minipage}{8cm}\begin{center}#1\end{center}\end{minipage}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\gdhsgmvoting}{%\parindent=0pt
  \par
本议案投同意票\underline{\hspace{1ex} 313,500,000\hspace{1ex}}股，同意票占有效表决票的\underline{\hspace{1ex} 100\hspace{1ex}}\%；\par
本议案投反对票\underline{\hspace{1ex} 0\hspace{1ex}}股，反对票占有效表决票的\underline{\hspace{1ex} 0\hspace{1ex}}\%；\par
本议案投弃权票\underline{\hspace{1ex} 0\hspace{1ex}}股，弃权票占有效表决票的\underline{\hspace{1ex} 0\hspace{1ex}}\%。\par
}
\newcommand{\gdhsgmvotingself}[6]{%\parindent=0pt
  \par
本议案投同意票\underline{\hspace{1ex} #1\hspace{1ex}}股，同意票占有效表决票的\underline{\hspace{1ex} #2\hspace{1ex}}\%；\par
本议案投反对票\underline{\hspace{1ex} #3\hspace{1ex}}股，反对票占有效表决票的\underline{\hspace{1ex} #4\hspace{1ex}}\%；\par
本议案投弃权票\underline{\hspace{1ex} #5\hspace{1ex}}股，弃权票占有效表决票的\underline{\hspace{1ex} #6\hspace{1ex}}\%。\par
}
%%%%%%%%%%%统计票数统计%%%%%%%%%%%%%%
\newcommand{\gmtongyi}[2]{%\parindent=0pt
  \par
本议案投同意票\underline{\hspace{1ex}#1\hspace{1ex}}股，同意票占有效表决票的\underline{\hspace{1ex}#2\%\hspace{1ex}}；
}
%%%%%%%%%%反对票数统计%%%%%%%%%%%%%%%%
\newcommand{\gmfandui}[2]{%\parindent=0pt
  \par
本议案投反对票\underline{\hspace{1ex}#1\hspace{1ex}}股，反对票占有效表决票的\underline{\hspace{1ex}#2\%\hspace{1ex}}；
}
%%%%%%%%%%%弃权票数统计%%%%%%%%%%%%%%%
\newcommand{\gmqiquan}[2]{%\parindent=0pt
  \par
本议案投弃权票\underline{\hspace{1ex}#1\hspace{1ex}}股，弃权票占有效表决票的\underline{\hspace{1ex}#2\%\hspace{1ex}}。
}
%%%%%%%%%%%%%%%
\newcommand{\gdhsbjtj}[8]{%\parindent=0pt
\par
%\begin{minipage}{\textwidth}
出席总股数：\underline{\hspace{1ex}#1\hspace{1ex}} 
投票股数： \underline{\hspace{1ex}#2\hspace{1ex}}\par
同\hspace{0.6ex}意\hspace{0.6ex}股\hspace{0.6ex}数：\underline{\hspace{1ex}#3\hspace{1ex}}
\hspace{1ex}反对股数：\underline{\hspace{1ex}#4\hspace{1ex}}\hspace{1ex}弃\hspace{0.4ex}权\hspace{0.4ex}股\hspace{0.4ex}数：\underline{\hspace{1ex}#5\hspace{1ex}} \par
同\hspace{1ex}意\hspace{1ex}率：\underline{\hspace{1ex}#6\%\hspace{1ex}}\hspace{1ex}反\hspace{1ex}对\hspace{1ex}率：\hspace{1em}\underline{\hspace{1ex}#7\%\hspace{1ex}}\hspace{1ex}弃\hspace{0.6ex}权\hspace{0.6ex}率：\underline{\hspace{1ex}#8\%\hspace{1ex}}
%\end{minipage} 
}
\newcommand{\gdhsbjtjconnected}[8]{%\parindent=0pt
\par
%\begin{minipage}{\textwidth}
出席总股数：\underline{\hspace{1ex}#1\hspace{1ex}} 
有投票权股数： \underline{\hspace{1ex}#2\hspace{1ex}}\par
同\hspace{0.6ex}意\hspace{0.6ex}股\hspace{0.6ex}数：\underline{\hspace{1ex}#3\hspace{1ex}}
\hspace{1ex}反对股数：\underline{\hspace{1ex}#4\hspace{1ex}}\hspace{1ex}弃\hspace{0.6ex}权\hspace{0.6ex}率：\underline{\hspace{1ex}#5\hspace{1ex}} \par
同\hspace{1ex}意\hspace{1ex}率：\underline{\hspace{1ex}#6\%\hspace{1ex}}\hspace{1ex}反\hspace{1ex}对\hspace{1ex}率：\hspace{1em}\underline{\hspace{1ex}#7\%\hspace{1ex}}\hspace{1ex}弃\hspace{0.6ex}权\hspace{0.6ex}率：\underline{\hspace{1ex}#8\%\hspace{1ex}}
%\end{minipage} 
}
%%%%%%%%%%%%%%%%%%
\newcommand{\gdhsjyh}[1]{\par{\parindent=0pt \xiaoerhao\heiti 议案 #1}}

\newcommand{\gdhsbm}[1]{
\myclearpage
\phantomsection
\addcontentsline{toc}{section}{#1}
}

\newcommand{\gdhsbmII}[1]{
\myclearpage
\phantomsection
\addcontentsline{toc}{subsection}{#1}
}

%%%%%%%%%%%%%%设置议案书签%%%%%%%%%%%%%
\newcommand{\gdhsbk}[1]{
\myclearpage
\phantomsection
\addcontentsline{toc}{section}{议案 #1}
{{\parindent=0pt \sanhao\heiti 议案 #1}}
}
%%%%%%%%%%%%%%%%股东大会统计决议情况签字栏%%%%%%%%%%%%%
\newcommand{\gdhsgdqm}{%
  \sanhao
\begin{minipage}{\textwidth}
\vspace*{1cm}
  统计员：\hspace{3em}\underline{\hspace{5cm}}
\vspace{1cm}

  计票及监票人：\underline{\hspace{5cm}} \\*[-2pt]
    \hspace*{11em}监事%\hspace{3cm}监事

\vspace{1cm}
\hspace*{7em}\underline{\hspace{5cm}} \hspace{1cm}\underline{\hspace{5cm}}\\*[-2pt]
\hspace*{10em}股东代表 \hspace{4cm}股东代表
\end{minipage} 
}
%%%%%%%%%%%%%%%%%%董事长、总经理署名%%%%%%%%%%%%%%%%
\newcommand{\gdhschairman}[1]{\hspace*{7cm}\parbox[c]{8cm}{\begin{center}\sanhao
广东华隧建设股份有限公司\par
董事长：方启超\par
#1\end{center}}}

\newcommand{\gdhspresident}[1]{\hspace*{7cm}\parbox[c]{8cm}{\begin{center}\sanhao
广东华隧建设股份有限公司\par
总经理：赵\hspace{1em}晖\par
#1\end{center}}}
%%%%%%%%董事会署名%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\gdhsboard}[1]{\hspace*{7cm}\parbox[c]{8cm}{\begin{center}\sanhao
广东华隧建设股份有限公司\par
董\hspace{1em}事\hspace{1em}会\par
#1\end{center}}}
%%%%%%%%监事会署名%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\gdhsjsh}[1]{\hspace*{7cm}\parbox[c]{8cm}{\begin{center}\sanhao
广东华隧建设股份有限公司\par
监\hspace{1em}事\hspace{1em}会\par
#1\end{center}}}
%%%%%%%%%%%%%%%%%%%%%%%%%
\iffalse
\newcounter{shuzi}
\usecounter{shuzi}
\setcounter{shuzi}{1}
%\newcommand{\Luolie}{(\arabic{shuzi})\addtocounter{shuzi}{1}}
\newcommand{\Luolie}{%
  \par{\bfseries 第\CJKnumber{\arabic{shuzi}}条\hspace{0.25em}} \addtocounter{shuzi} {-1}\refstepcounter{shuzi}\addtocounter{shuzi}{1}}
\fi
%%%%%%%%%设计计数器%%%%%%%%%%%%%%%
\newcounter{shuzi}
\usecounter{shuzi}
\setcounter{shuzi}{1}
%\newcommand{\Luolie}{(\arabic{shuzi})\addtocounter{shuzi}{1}}
\newcounter{shuziI}
\usecounter{shuziI}
%%%%%%
\newcounter{shuziII}
\usecounter{shuziII}
%%%%%%%%%%%%%
\newcounter{shuziIII}
\usecounter{shuziIII}
%%%%%%%%%设计层级列数%%%%%%%
\newcommand{\Luolie}{%
\par{\bfseries 第\CJKnumber{\arabic{shuzi}}条\hspace{0.25em}} \addtocounter{shuzi} {-1}\refstepcounter{shuzi}\addtocounter{shuzi}{1}%
\setcounter{shuziI}{1}%
}
%\newcommand{\Luolie}{(\arabic{shuzi})\addtocounter{shuzi}{1}}
\newcommand{\LuolieI}{%
  \par{\bfseries (\CJKnumber{\arabic{shuziI}})\hspace{0.25em}} \addtocounter{shuziI} {-1}\refstepcounter{shuziI}\addtocounter{shuziI}{1}%
\setcounter{shuziII}{1}%
}
%%%%%%%%%%%%%%%
\newcommand{\LuolieII}{%
  \par{\bfseries \arabic{shuziII}.\hspace{0.25em}} \addtocounter{shuziII} {-1}\refstepcounter{shuziII}\addtocounter{shuziII}{1}%
\setcounter{shuziIII}{1}%
}
%%%%%%%%%%%%%%%%%%%%
\newcommand{\LuolieIII}{%
  \par{\bfseries (\arabic{shuziIII})\hspace{0.25em}} \addtocounter{shuziIII} {-1}\refstepcounter{shuziIII}\addtocounter{shuziIII}{1}%
}
%%%%%%%%%%%%%%%%%%%主要用于协议文本中%%%%%%%%%%%%%%%%%%%%%
\ifxieyibk
\newcounter{xieyi}
\usecounter{xieyi}
\setcounter{xieyi}{1}
%\newcommand{\Luolie}{(\arabic{shuzi})\addtocounter{shuzi}{1}}
\newcounter{xieyiI}
\usecounter{xieyiI}
%%%%%%
\newcounter{xieyiII}
\usecounter{xieyiII}
%%%%%%%%%%%%%
\newcounter{xieyiIII}
\usecounter{xieyiIII}
%%%%%%%%%设计层级列数%%%%%%%
\newcommand{\Xieyi}[1]{%
\par
  \parindent=0pt
  {\bfseries 第\CJKnumber{\arabic{xieyi}}条\hspace{0.2em}#1}\addtocounter{xieyi}{1}%
\addtocounter{xieyi} {-1}
\phantomsection
\addcontentsline{toc}{section}{第\CJKnumber{\arabic{xieyi}}条\hspace{0.2em}#1}
%\titlecontents{section}[0pt]{\addvspace{2pt}\filright}{\contentspush{\thecontentslabel\ }}{}{\titlerule*[8pt]{.}\contentspage}
%\contentsline{section}{\numberline{12.8}第\CJKnumber{\arabic{xieyi}}条\hspace{0.2em}#1}{\contentspage}
\addtocounter{xieyi} {1}
\setcounter{xieyiI}{1}%
}
%%%%%%%%%%
\newcounter{xieyiXH}
\usecounter{xieyiXH}
\setcounter{xieyiXH}{1}
%%%
\newcommand{\XieyiXH}{%
\par
 \parindent=-1em
  \hangafter 1
　\hangindent 1.25em
  \parindent=0pt
  \arabic{xieyiXH}.\hspace{0.2em}\addtocounter{xieyiXH}{1}%
}
%%%%%%%%%
\newcommand{\NXieyiXH}{%
\par
 \parindent=0.35em
  \hangafter 1
　\hangindent 1.5em
%  \parindent=0pt
 }
%%%%%%%%%%%%%%%%%%%%
\newcommand{\XieyiI}{%
  \par
    \parindent=0.5em
  \hangafter 1
　\hangindent 3.75em
\addtocounter{xieyi} {-1}
  {\arabic{xieyi}.\arabic{xieyiI}\hspace{0.2em}} \addtocounter{xieyiI} {-1}\refstepcounter{xieyiI}\addtocounter{xieyiI}{1}%
  \addtocounter{xieyi} {1}
\setcounter{xieyiII}{1}%
}
%%%
\newcommand{\NXieyiI}{%
  \par
    \parindent=2.75em
  \hangafter 1
　\hangindent 3.75em
}
%%%%%%%%%%%%%%%
\newcommand{\XieyiII}{%
  \par
    \parindent=2.5em
  \hangafter 1
　\hangindent 7em
%　\noindent
\addtocounter{xieyi} {-1}
\addtocounter{xieyiI} {-1}
    \arabic{xieyi}.\arabic{xieyiI}.\arabic{xieyiII}\hspace{0.2em} \addtocounter{xieyiII} {-1}\refstepcounter{xieyiII}\addtocounter{xieyiII}{1}%
\addtocounter{xieyi} {1}
\addtocounter{xieyiI} {1}
\setcounter{xieyiIII}{1}%
}
%%%%%
\newcommand{\NXieyiII}{%
  \par
    \parindent=2.5em
  \hangafter 1
　\hangindent 7em
%　\noindent
}
%%%%%%%%%%%%%%%%%%%%
\newcommand{\XieyiIII}{%
  \par{\bfseries (\arabic{xieyiIII})\hspace{0.25em}} \addtocounter{xieyiIII} {-1}\refstepcounter{xieyiIII}\addtocounter{xieyiIII}{1}%
}
\fi
%%%%%%%%%%%董事会届次%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcounter{myshuzij}
\usecounter{myshuzij}
\setcounter{myshuzij}{1}
\newcommand{\jj}{\CJKnumber{\arabic{myshuzij}}}
\newcounter{myshuzijc}
\usecounter{myshuzijc}
\setcounter{myshuzijc}{1}
\newcommand{\jc}{\CJKnumber{\arabic{myshuzijc}}}
\newcommand{\bjc}{\gdhsbmII{第\jj届董事会第\jc次会议}\addtocounter{myshuzijc}{1}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%董事会决议设置页面
\newcounter{pageshuzi}
\usecounter{pageshuzi}
\newcommand{\boardcover}[1]{
\begin{titlepage}
\vspace*{4.5cm}
\begin{center}
\setcounter{pageshuzi}{\arabic{myshuzijc}-1}
{\fontsize{28pt}{28pt}\selectfont

{\bfseries\hwzhongsong \textcolor{red}{广东华隧建设股份有限公司}}


\begin{minipage}[b]{16cm}
\begin{tikzpicture}[remember picture,overlay]
\path [draw,line width=1.3mm,color=red] (0,0.6) -- (16,0.6);  
\path [draw,line width=0.6mm,color=red] (0,0.4) -- (16,0.4); 
\end{tikzpicture}
\end{minipage}

}


\fangsong
\vspace{4.5cm}
\erhao
{\hwzhongsong 第\jj届董事会第\CJKnumber{\arabic{pageshuzi}}次会议}

\vspace{8cm}
\xiaoerhao
{\hwzs #1}

\vspace{2.5cm}
广东华隧建设股份有限公司会议室
\end{center}
\end{titlepage}
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%监事会届次
\newcounter{mshuzij}
\usecounter{mshuzij}
\setcounter{mshuzij}{1}
\newcommand{\mjj}{\CJKnumber{\arabic{mshuzij}}}
\newcounter{mshuzijc}
\usecounter{mshuzijc}
\setcounter{mshuzijc}{1}
\newcommand{\mjc}{\CJKnumber{\arabic{mshuzijc}}}
\newcommand{\smjc}{\gdhsbmII{第\mjj届监事会第\mjc次会议}\addtocounter{mshuzijc}{1}}
%%%%%%%%%%%%%%%%%%%%%%
%监事会决议设置页面
\newcounter{jspageshuzi}
\usecounter{jspageshuzi}
\newcommand{\jscover}[1]{
\begin{titlepage}
\vspace*{4.5cm}
\begin{center}
\setcounter{jspageshuzi}{\arabic{mshuzijc}-1}
{\fontsize{28pt}{28pt}\selectfont

{\bfseries\hwzhongsong \textcolor{red}{广东华隧建设股份有限公司}}

%\parindent=0pt
\begin{minipage}[b]{16cm}
\begin{tikzpicture}[remember picture,overlay]
\path [draw,line width=1.3mm,color=red] (0,0.6) -- (16,0.6);  
\path [draw,line width=0.6mm,color=red] (0,0.4) -- (16,0.4); 
\end{tikzpicture}
\end{minipage}

}


\fangsong
\vspace{4.5cm}
\erhao
{\hwzhongsong 第\msjj届监事会第\CJKnumber{\arabic{jspageshuzi}}次会议}

\vspace{8cm}
\xiaoerhao
{\hwzs #1}

\vspace{2.5cm}
广东华隧建设股份有限公司会议室
\end{center}
\end{titlepage}
}
%%%%%%%%%%%%%%%%%%%%%%%%%
%股东大会封面
\newcommand{\gmcover}[2]{
\begin{titlepage}
\vspace*{4.5cm}
\begin{center}
{
\fontsize{32pt}{32pt}\selectfont
{\hwzhongsong \textcolor{red}{%\hspace{1.15ex}
广东华隧建设股份有限公司}}\vspace*{6mm}

\begin{minipage}[h]{16cm}
\begin{tikzpicture}[remember picture,overlay]
\path [draw,line width=1.3mm,color=red] (0,0.6) -- (16,0.6);  
\path [draw,line width=0.6mm,color=red] (0,0.4) -- (16,0.4); 
\end{tikzpicture}
\end{minipage}
}
%\vspace*{1.95mm}



\vspace{2.5cm}

\fangsong
\erhao
{\hwzhongsong #1}

\vspace{8cm}
\xiaoerhao
{\hwzhongsong #2}

\vspace{2.5cm}
广东华隧建设股份有限公司会议室
\end{center}
\end{titlepage}
}
%%%%%%%%%%%旁边注释%%%%%%%%
\newlength{\yellownotewidth}
\setlength{\yellownotewidth}{2cm}
\newlength{\yellownoteheight}
\setlength{\yellownoteheight}{2cm}
\newcommand{\yellownote}[1]{
\marginpar{
\vspace{-0.5\yellownoteheight}
\begin{center}
\begin{tikzpicture}
\draw[white,fill=gray!25,opacity=0.75,shift={(-0.125,-0.125)}]
(0,0) rectangle (\yellownotewidth,\yellownoteheight);
\draw[fill=yellow!35] (0,0) rectangle (\yellownotewidth,\yellownoteheight);
\draw[opacity=0.45,fill=gray!50] (0.7\yellownotewidth,0) --
(0.9\yellownotewidth,0.45) -- (\yellownotewidth,0.4) -- cycle;
\node[blue,below] at (0.5\yellownotewidth,\yellownoteheight) {
\begin{minipage}{\yellownotewidth-1em}
\scriptsize\sf#1
\end{minipage}
};
\end{tikzpicture}
\end{center}
\vspace{0.5\yellownoteheight}
}
}
%%%%%%%%%%%
\newcommand{\resizeableyellownote}[3]{
\setlength{\yellownotewidth}{#1cm}
\setlength{\yellownoteheight}{#2cm}
\marginpar{
\vspace{-0.5\yellownoteheight}
\begin{center}
\begin{tikzpicture}
\draw[white,fill=gray!25,opacity=0.75,shift={(-0.125,-0.125)}]
(0,0) rectangle (\yellownotewidth,\yellownoteheight);
\draw[fill=yellow!35] (0,0) rectangle (\yellownotewidth,\yellownoteheight);
\draw[opacity=0.45,fill=gray!50] (0.7\yellownotewidth,0) --
(0.9\yellownotewidth,0.45) -- (\yellownotewidth,0.4) -- cycle;
\node[blue,below] at (0.5\yellownotewidth,\yellownoteheight) {
\begin{minipage}{\yellownotewidth-1em}
\scriptsize\sf#3
\end{minipage}
};
\end{tikzpicture}
\end{center}
\vspace{0.5\yellownoteheight}
}
}
%%%%%%%%%%页面水印设置%%%%%%%%
\newcommand\BackgroundPicturelinux{%
   \put(0,0){%
     \parbox[b][\paperheight]{\paperwidth}{%
       \vfill
      \centering
\color{red}
\vspace*{25.5cm}
%\gdhsbline
\begin{flushleft}
\parindent=0pt
\begin{tikzpicture}[remember picture,overlay]
\path [draw,line width=2mm,color=red] (2.5,1) -- (18.5,1);  
\path [draw,line width=1mm,color=red] (2.5,0.8) -- (18.5,0.8); 
\end{tikzpicture}
\end{flushleft}
     }}}
%%%%%%%%%页面水印设置%%%%%%%%%%
\newcommand\BackgroundPicturewin{%
   \put(0,0){%
     \parbox[b][\paperheight]{\paperwidth}{%
       \vfill
      \centering
\color{red}
\vspace*{25.5cm}
%\gdhsbline
\rule{\textwidth}{1pt}\\*[-8pt]\rule[5mm]{\textwidth}{3pt}
       \vfill
     }}}
%\AddToShipoutPicture{\BackgroundPicture}%增加
%\ClearShipoutPicture%去掉
%%%%%%%%%%%%%%%%%%套公司的红头文件%%%%%%%%%%%%%%%%%%
\newcommand{\taohongtou}[1]{
\begin{center}
{\renewcommand{\CJKglue}{\hskip 3pt plus 0.1\baselineskip}%设置字间距
{\fzxbs\fontsize{32pt}{32pt}\selectfont%\bfseries 
\textcolor{red}{%\parindent=0pt
广东华隧建设股份有限公司}}}
\end{center}
\vspace*{-4mm}

\begin{flushleft}
%\parindent=0pt
\begin{minipage}[b]{16cm}
\begin{tikzpicture}[remember picture,overlay]
\path [draw,line width=1.3mm,color=red] (0,0.9) -- (\textwidth,0.9);  
\path [draw,line width=0.6mm,color=red] (0,0.75) -- (\textwidth,0.75); 
%\draw [line width=1mm,opacity=.25]
%(current page.south) circle (3cm);
\end{tikzpicture}
\end{minipage}
\end{flushleft}
\begin{center}
{\fzxbs\erhao #1}
\end{center}
\vspace{1ex}
}
%%%%%%%%%%底部红线%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand\BackgroundPictureredline{%
   \put(0,0){%
     \parbox[b][\paperheight]{\paperwidth}{%
%       \vfill
      \centering
%\color{red}
\vspace*{22cm}
%\gdhsbline
\begin{flushleft}
\parindent=0pt
\begin{tikzpicture}[remember picture,overlay]
\path [draw,line width=1.3mm,color=red] (2.2,1) -- (18.8,1);  
\path [draw,line width=0.6mm,color=red] (2.2,0.85) -- (18.8,0.85); 
\end{tikzpicture}
\end{flushleft}
     }}}
%\AddToShipoutPicture{\BackgroundPicturegdhsred}%增加
%\ClearShipoutPicturegdhsred%去掉
%%%%%%%%%%签名设置%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\sign}[1]{{\parindent=1em
\parbox[c]{4cm}{
\begin{tikzpicture}[remember picture,overlay]
\path [draw,line width=1pt,color=black] (0,1) -- (4,1);
\end{tikzpicture}
\vspace*{-1.5cm}
\begin{center}
#1
\end{center}}}\hspace{1.5cm}}
%%%%%%%%%%%%%%议案标题设置%%%
\newcommand{\yian}[1]{{\fzxbs\erhao \begin{center} #1\end{center}}\vspace{2em}}
\newcommand{\myunderline}[1]{\underline{\hspace{1.5ex}#1\hspace{1.5ex}}}
\newcommand{\juzhong}[1]{{\parindent=0pt
\begin{center} #1\end{center}}}
\newcommand{\chuti}[1]{{\bf{#1}}}
\newcommand{\pchuti}[1]{\par{\bf{#1}}\par}
\newcommand{\minitab}[2][l]{\begin{tabular}{#1}#2\end{tabular}} 
%%%%%%%%
\newcounter{myres}
\usecounter{myres}
\setcounter{myres}{1}
\newcommand{\Jueyi}{%
\par{\bfseries 决议\CJKnumber{\arabic{myres}}：\hspace{0.1em}} \addtocounter{myres} {-1}\refstepcounter{myres}\addtocounter{myres}{1}%
}
%%%%%%%%%%%%%%%
\newcounter{mypros}
\usecounter{mypros}
\setcounter{mypros}{1}
\newcommand{\mypros}{%
\par 议案\arabic{mypros}：\hspace{0.1em} \addtocounter{mypros}{-1}\refstepcounter{mypros}\addtocounter{mypros}{1}%
}
%%%%%%%%%%%%%%%%%
\newcounter{xuhao}
\usecounter{xuhao}
\setcounter{xuhao}{1}
\newcounter{xuhaoI}
\usecounter{xuhaoI}
\newcommand{\XH}{\arabic{xuhao}\addtocounter{xuhao}{1}
\setcounter{xuhaoI}{1}}
\newcommand{\XHI}{\addtocounter{xuhao}{-1}
\arabic{xuhao}.\arabic{xuhaoI}\addtocounter{xuhaoI}{1}\addtocounter{xuhao}{1}}

%%%%%%%%%%%%%%%%%
%%设置罗马数字
\makeatletter
\newcommand{\rmnum}[1]{\romannumeral #1}
%小写的罗马字符 \romannumeral 4 表示
\newcommand{\Rmnum}[1]{\expandafter\@slowromancap\romannumeral #1@}
%大写的罗马字符用 \uppercase\expandafter{\romannumeral 4} 表示
\makeatother
%%%%%%%%%%%%%%%%%%%%%%%
\ifmemo
%上市工作会议纪要
\newcommand{\attend}[4]{
\begin{tabularx}{\textwidth}{lX}
\hline
\textbf{参会人员:}&#1\\
\textbf{会议时间：}&#2\\
\textbf{会议地点：}&#3\\
\textbf{主\hspace{2em}题:}&#4\\\hline
\end{tabularx}
}

\newcommand{\memotile}[1]{
{{\parindent=0pt\erhao\bfseries\kaiti\begin{center}#1\end{center}}\vspace{1em}}
}
\newcommand{\memoattend}[1]{{\parindent=0pt \rule{\textwidth}{1pt}}\par
\parbox[t]{5em}{\textbf{参会人员:}}\hspace{2ex}\parbox[t]{12cm}{#1}%{\vspace{2ex}}
}

\newcommand{\memotime}[1]{\vspace{1em}\parbox[t]{5em}{\textbf{会议时间：}}\hspace{2ex}\parbox[t]{\textwidth-5em-2ex}{#1}%{\vspace{1ex}}
}
\newcommand{\memoaddress}[1]{\parbox[t]{5em}{\textbf{会议地点：}}\hspace{2ex}\parbox[t]{\textwidth-5em-2ex}{#1}%{\vspace{1ex}}
}
\newcommand{\memosubject}[1]{\parbox[t]{5em}{\textbf{主\hspace{2em}题:}}\hspace{2ex}\parbox[t]{\textwidth-5em-2ex}{#1}
\par
{\parindent=0pt \rule[1em]{\textwidth}{1pt}}
}

\renewpagestyle{plain}{
 \sethead[][][{\kaiti\wuhao华隧建设发行上市项目会议纪要}]
%  \sethead[][][{\headfont{}\thesissubject}] % 页眉偶数页，五号字体，居右
%  {}{}{{\headfont{}\sectiontitle}} % 页眉奇数页，五号字体，居中
{}{}{{\kaiti\wuhao华隧建设发行上市项目会议纪要}} % 页眉奇数页，五号字体，居右
  \setfoot{}{{\headfont{}\wuhao \thepage}}{}%页码五号宋体居中
  \headrule%上横线
  \setheadrule{1.5pt}%设置横线粗细
}

\newpagestyle{myplain}{
 %\sethead[][][{\kaiti\wuhao华隧建设发行上市项目会议纪要}]
%  \sethead[][][{\headfont{}\thesissubject}] % 页眉偶数页，五号字体，居右
%  {}{}{{\headfont{}\sectiontitle}} % 页眉奇数页，五号字体，居中
%{}{}{{\kaiti\wuhao华隧建设发行上市项目会议纪要}} % 页眉奇数页，五号字体，居右
  \setfoot{}{{\wuhao \thepage}}{}%页码五号宋体居中
%  \headrule%上横线
%  \setheadrule{1.5pt}%设置横线粗细
}

\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newpagestyle{myplainI}{
 %\sethead[][][{\kaiti\wuhao华隧建设发行上市项目会议纪要}]
%  \sethead[][][{\headfont{}\thesissubject}] % 页眉偶数页，五号字体，居右
%  {}{}{{\headfont{}\sectiontitle}} % 页眉奇数页，五号字体，居中
%{}{}{{\kaiti\wuhao华隧建设发行上市项目会议纪要}} % 页眉奇数页，五号字体，居右
  \setfoot{}{{\wuhao \thepage{} / \pageref{LastPage}}}{}%页码五号宋体居中
%  \headrule%上横线
%  \setheadrule{1.5pt}%设置横线粗细
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{pifont}
\newcommand{\BMsignature}{
\newpage
\juzhong{[本页无正文，为\Nameofmeeting 决议签署页]}
\vspace{1.5em}\par
 董事签名:
\vspace{7.5em}\par
\sign{赵\hspace{1em}晖}\sign{彭迎春}\sign{王\hspace{1em}昭}
\vspace{7.5em}\par
\sign{钟晓晖}\sign{戴智波}\sign{郭美文}
\vspace{7.5em}\par
\sign{卢光霖}\sign{谢\hspace{1em}军}\sign{周\hspace{1em}兵}
\vspace{5em}\par
%\md{广东华隧建设股份有限公司}
\md{\dateofmeeting}
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\BMsignatureI}{%%%董事会董事签字页，需要输入第几次会议，形成决议时间
\newpage
\parindent=2.1em
\juzhong{[本页无正文，为\Nameofmeeting
决议签署页]}
\vspace{1.5em}
 董事签名:
\vspace{1cm}\par
\parindent=-2.5cm
\begin{minipage}{21cm}
\begin{center}
\includegraphics[scale=0.32,keepaspectratio]{BMsignatureI.jpg}
\end{center}
\end{minipage}
\vspace{1cm}
\parindent=2.5cm
\parindent=2.1em\par
\md{\dateofmeeting}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\SMsignatureI}{%%%监事会监事签字页，需要输入第几次会议，形成决议时间
\newpage
\parindent=2.1em
\juzhong{[本页无正文，为\Nameofmeeting
决议签署页]}
\vspace{1.5em}\par
监事签名:\par
\parindent=-2.5cm
\begin{minipage}{21cm}
\begin{center}
\includegraphics[scale=0.33,keepaspectratio]{SMsignatureI.jpg}
\end{center}
\end{minipage}
%\vspace{1cm}
\parindent=2.5cm
\parindent=2.1em\par
\md{\dateofmeeting}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\SMsignature}{
\newpage
\begin{center}
[本页无正文，为\Nameofmeeting
决议签署页]
\end{center}
\vspace{1cm}\par
监事签名:
\vspace{5.5cm}\par
\sign{郑舒秋}\sign{李康安}\sign{张万鑫}
\vspace{4cm}\par
%\md{广东华隧建设股份有限公司}
\md{\dateofmeeting}}
%%%%%%%%%加盖公司章%
\setlength{\unitlength}{1cm}
\newcommand{\boardlogo}[1]{
\newcommand\Backgroundboard{
\put(350,1200){
\parbox[c][4cm]{4cm}{%
\vfill
\centering
\includegraphics[scale=0.5,keepaspectratio]{board.jpg}%scale of board and office = about 1; scale of jianshihui =0.3
\vfill
}}}
\hspace{7cm}\begin{minipage}{8cm}
\AddToShipoutPicture{\Backgroundboard}
\begin{center}
广东华隧建设股份有限公司\par
董\hspace{1em}事\hspace{1em}会\par
#1
\end{center}
\end{minipage}}
%%%%%%%%股东大会决议签署页%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\gmsignature}{%
\newpage
%\parindent=0pt
\begin{center}[本页无正文，为\Nameofmeeting
决议签字页]\end{center}
\vspace{0.6em}\par
{\heiti 股东及股东委托代理人签名并盖章：}
\vspace*{1cm}\par
广东省建筑工程集团有限公司
\vspace{2.6cm}\par
广东省基础工程公司
\vspace{2.6cm}\par
广东省工业设备安装公司
\vspace{2.6cm}\par
广东中科白云创业投资有限公司
\vspace{2.6cm}\par
广东恒健投资控股有限公司
\vspace{2.6cm}\par
\md{\dateofmeeting}
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\myvspace}{\vspace{5em}\par}
\newcommand{\gmallsignature}{%
\newpage
%\parindent=0pt
\begin{center}[本页无正文，为\Nameofmeeting决议签字页]\end{center}
\vspace{0.6em}\par
{\heiti 股东及股东委托代理人签名并盖章：}
\vspace*{1cm}\par
广东省建筑工程集团有限公司
\vspace{3cm}\par
广东省基础工程公司
\vspace{3cm}\par
广东省工业设备安装公司
\vspace{3cm}\par
广东中科白云创业投资有限公司
\vspace{3cm}\par
广东恒健投资控股有限公司
\vspace{3cm}\par
%%%%%%%%%%%%%%
\newpage
\begin{center}[本页无正文，为\Nameofmeeting决议签字页]\end{center}
\myvspace                                
\sign{赵\hspace{1em}晖}\sign{易\hspace{1em}觉}\sign{王\hspace{1em}昭}\myvspace
\sign{赖伟文}\sign{蔡国贤}\sign{黄美珍}\myvspace
\sign{李康安}\sign{ 刘文革}\sign{ 詹国良}\myvspace
\sign{龚仁芳}\sign{凌\hspace{1em}波}\sign{周振宇}\myvspace
\sign{刘  威}\sign{彭衡湘}\sign{陈士明}\myvspace
%%%%%%%%%%%%%%%%%%%%
\newpage
\begin{center}[本页无正文，为\Nameofmeeting决议签字页]\end{center}
\myvspace
\sign{王小军}\sign{刘\hspace{1em}玮}\sign{何\hspace{1em}伦}\myvspace
\sign{陈少锋}\sign{陈钦东}\sign{汤\hspace{1em}泳}\myvspace
\sign{蔡丽辉}\sign{朱劲锋}\sign{周焕明}\myvspace
\sign{黎向平}\sign{林清基}\sign{张细妹}\myvspace
\sign{周任锋}\sign{陈泽灵}\sign{刘恕全}\myvspace
%%%%%%%%%%%%%%%%%
\newpage
\begin{center}[本页无正文，为\Nameofmeeting决议签字页]\end{center}
\myvspace
\sign{李楚平}\sign{孙建敏}\sign{李\hspace{1em}奕}\myvspace
\sign{陈小勇}\sign{王永贵}\sign{董维奇}\myvspace
\sign{吴海升}\sign{吕明豪}\sign{马升雁}\myvspace
\sign{李\hspace{1em}飞}\sign{黄浩锋}\sign{杨自华}\myvspace
\sign{沈云泽}\sign{陈  杰}\sign{刘冠升}\myvspace
%%%%%%%%%%%%%%%%%
\newpage
\begin{center}[本页无正文，为\Nameofmeeting决议签字页]\end{center}
\myvspace
\sign{温娟子}\sign{张志勇}\sign{李\hspace{1em}江}\myvspace
\sign{方俊生}\sign{罗伟均}\sign{郑永龙}\myvspace
\sign{陈伟彬}\sign{夏文韬}\sign{戴哲权}\myvspace
\sign{林\hspace{1em}东}\sign{黄\hspace{1em}强}\myvspace

\md{\dateofmeeting}
}
%%%%%%%%%%%%%%%

\renewcommand{\normalsize}{\xiaosanhao\fangsong}
\AtBeginDocument{%\CJKindent{}%
    \parindent=2.1em
    %\makeindex%
    \normalsize%正文字体格式
    \linespacing{1.682}% 主行距～1.5倍
    %\setlength{\baselineskip}{28pt}
  }
\AtEndDocument{}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\endinput
%%%%%%%%%%%%%%%%%%%%%%%%% End of file `scutthesis.cls'.
