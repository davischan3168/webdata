\NeedsTeXFormat{LaTeX2e}[1999/12/01]
\ProvidesClass{mypptall}[2011/03/31 2.0.1 The LaTeX class for presatation and print documents]

\newif\ifprint\printfalse % 使用xeCJK设置字体，
\DeclareOption{print}{\printtrue} % 

\newif\ifpres\presfalse % for gdhs only
\DeclareOption{pres}{\prestrue} % 

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions
\LoadClass{article}
%\documentclass[12pt,reqno]{article}%for print only

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\ifprint
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

\usepackage{anysize,mathrsfs,multicol,amsmath,amsthm}
\marginsize{15mm}{15mm}{15mm}{15mm}

\usepackage{color,amssymb}

\usepackage{wasysym}

\definecolor{zi}{rgb}{1,0.75,1}
\newcommand{\h}{\hspace*{1pt}}
\newtheoremstyle{mythm}{1.1ex}{1.1ex}{\it}{}{}{}{ }{\colorbox{zi}{\h\emph{\thmname{#1}\thmnumber{ #2}\thmnote{ (#3)}\rule[-0.5ex]{0ex}{2.4ex}.}\h}}
\theoremstyle{mythm}
\newtheorem{theorem}{Thm}
\newtheorem{proposition}[theorem]{Pro}
\newtheorem{corollary}[theorem]{Cor}
\newtheorem{example}[theorem]{Exm}
\newtheorem{definition}[theorem]{Def}
\newtheorem{lemma}[theorem]{Lem}
\newtheorem{claim}[theorem]{Clm}
\newtheorem{remark}[theorem]{Rek}
\renewcommand{\mathcal}{\mathscr}
\renewcommand{\emph}[1]{\textcolor[rgb]{0.00,0.00,0.60}{#1}}
\definecolor{orange}{rgb}{0.7,0.0,0.0}
\newcommand{\emp}[1]{\textcolor{orange}{#1}}
\newcommand{\pause}{\rule{0.3ex}{1.5ex}}

%\renewcommand{\int}{\varint}

\newtheoremstyle{PF}{1.1ex}{1.1ex}{}{}{}{}{ }{\colorbox{zi}{\h\emph{\thmname{#1}\thmnote{ of #3}\rule[-0.5ex]{0ex}{2.4ex}.}\h}}
\theoremstyle{PF}
\newtheorem{Pf}{Pf}
\fi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\ifpres
\usepackage{arev,amsthm,ifthen,picins,pause,fancyhdr}
%\usepackage{background}
%\usepackage{mpmulti}
\usepackage[screen,sectionbreak]{pdfscreen}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}
\RequirePackage[UTF8]{ctex}
\RequirePackage{times}
\RequirePackage{CJKnumb}

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

\definecolor{zi}{rgb}{1,0.75,1}
\newcommand{\h}{\hspace*{1pt}}
\newtheoremstyle{mythm}{1.1ex}{1.1ex}{\it}{}{}{}{ }{\colorbox{zi}{\h\emph{\thmname{#1}\thmnumber{ #2}\thmnote{ (#3)}\rule[-0.5ex]{0ex}{2.4ex}.}\h}}
\theoremstyle{mythm}
\newtheorem{theorem}{Thm}
\newtheorem{proposition}[theorem]{Pro}
\newtheorem{corollary}[theorem]{Cor}
\newtheorem{example}[theorem]{Exm}
\newtheorem{definition}[theorem]{Def}
\newtheorem{lemma}[theorem]{Lem}
\newtheorem{claim}[theorem]{Clm}
\newtheoremstyle{myrek}{1.1ex}{1.1ex}{}{}{}{}{ }{\colorbox{zi}{\h\emph{\thmname{#1}\thmnumber{ #2}\thmnote{ (#3)}\rule[-0.5ex]{0ex}{2.4ex}.}\h}}
\theoremstyle{myrek}
\newtheorem{remark}[theorem]{Rek}
\renewcommand{\mathcal}{\mathrm}

\renewcommand{\figurename}{Fig}
\margins{2mm}{2mm}{7mm}{2mm} \screensize{85mm}{113.4mm}
\renewcommand{\emph}[1]{\textcolor[rgb]{0.00,0.00,0.60}{#1}}
\parindent=0ex
\newtheoremstyle{PF}{1.1ex}{1.1ex}{\sf}{}{\sf}{}{ }{\colorbox{zi}{\h\emph{\thmname{#1}\thmnote{ of #3}\rule[-0.5ex]{0ex}{2.4ex}.}\h}}
\theoremstyle{PF}
\newtheorem{Pf}{Pf}
\hypersetup{CJKbookmarks={true}} 
\allowdisplaybreaks

\AtBeginDocument{\sffamily\pagedissolve{Dissolve/D
0.1}
\overlay{back}
\youyuan
%\begin{CJK*}{GBK}{you}
\CJKtilde\sloppy}

\AtEndDocument{
  \tableofcontents\hypertarget{cont}{}
%\end{CJK*}
}

\renewcommand{\theenumi}{\rm\textcolor[rgb]{0,0.5,0}{(\roman{enumi})}}
\renewcommand{\labelenumi}{\theenumi}
\renewcommand{\qed}{\hfill\fbox{\textcolor[rgb]{0,0,1}{\rule{1ex}{1ex}}}}
\definecolor{red}{rgb}{0.0,0.00,0.6}
\definecolor{orange}{rgb}{0.6,0.0,0.0}
\newcommand{\emp}[1]{\textcolor{orange}{#1}}
\renewcommand{\headrulewidth}{0pt}

\newcommand{\yel}[1]{\textcolor[rgb]{1.00,1.00,0.50}{#1}}
\pagestyle{fancy}\fancyhf{}

\fancyhead[L]{\raisebox{-78.5mm}{
\fontsize{7pt}{8pt}\selectfont\hyperlink{cont}{\yel{\thepage/25}}}}

\fancyhead[R]{\raisebox{-78.5mm}{\fontsize{7pt}{8pt}\selectfont\Acrobatmenu{GoBack}{\yel{7th
AIMS Conf, 2008}}\quad\Acrobatmenu{Quit}{\yel{S.B. Liu}}}}
\hypersetup{pdfpagemode={FullScreen}}
\fi
%%The end of CLS%%
