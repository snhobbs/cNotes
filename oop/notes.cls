\ProvidesClass{notes}

\LoadClass[11pt, noindent, oneside]{memoir}
\usepackage[left=.75in, right=.75in, top=1in, bottom=1in]{geometry}
\setlength\parindent{0pt}
\setlength\textwidth{7in}

\makechapterstyle{AlexanderGrebenkov}{%
\renewcommand{\chapterheadstart}{\vspace
*
{\beforechapskip}\hrule\medskip}
\renewcommand{\chapnamefont}{\normalfont\large\scshape}
\renewcommand{\chapnumfont}{\normalfont\large\scshape}
\renewcommand{\chaptitlefont}{\normalfont\large\scshape}
\renewcommand{\printchaptername}{\S}
\renewcommand{\chapternamenum}{ }
\renewcommand{\printchapternum}{\chapnumfont \thechapter}
\renewcommand{\afterchapternum}{. }
\renewcommand{\afterchaptertitle}{\par\nobreak\medskip\hrule\vskip
\afterchapskip}
}
%\chapterstyle{AlexanderGrebenkov}
\chapterstyle{ell}

\usepackage{graphicx}
\usepackage{longtable}
\settocdepth{subsection}

% ****************************************
%\makepagestyle{pageEscape}
\copypagestyle{heading}{pageEscape}
%\makeevenfoot{pageEscape}{}{}{}
%\makeoddfoot{pageEscape}{}{}{}


\usepackage{xcolor}%
\definecolor{darkblue}{RGB}{0,0,150}
\definecolor{lightgray}{RGB}{220,220,220}
\definecolor{lightblue}{RGB}{70,150,250}
\definecolor{lightred}{RGB}{250,180,150}
\definecolor{paleyellow}{RGB}{255,255,101}
\definecolor{amber}{rgb}{1.0, 0.49, 0.0}
\definecolor{a}{RGB}{250,150,70}
\definecolor{b}{RGB}{200,150,70}
\definecolor{c}{RGB}{150,150,70}

\usepackage{bytefield}
\newcommand{\colorbitbox}[3]{%
\rlap{\bitbox{#2}{\color{#1}\rule{\width}{\height}}}%
\bitbox{#2}{#3}}

\usepackage[linkbordercolor = darkblue, linkcolor=darkblue, urlcolor=darkblue, colorlinks=true]{hyperref}

\newcommand{\opt}[1]{$<$#1$>$}
\newcommand{\ra}{$\rightarrow$ {}}
\newcommand{\rsrc}[1]{\hspace{44pt}\textbf{#1: }}
\newcommand{\blank}{\_\_\_\_{} }
\newcommand{\FIXME}[1]{\textbf{\{FIXME: #1}\}}
\newcounter{questionSec}
\newcounter{questionCount}[questionSec]
\newcommand{\qItem}[2]{\stepcounter{questionCount} \textbf{\thequestionCount} & #1 & #2\\\hline}
\newcommand{\qes}[2]{\item \textbf{#1 : }#2}

\newenvironment{questions}[1]{\subsection{#1}
	%\centering{\large\textbf{#1}}\\
	%\vspace{2pt}\hrule\vspace{12pt}

	\newenvironment{questionAnswer}{
		\begin{longtable}{|r| p{.35\textwidth}|p{.55\textwidth}|}
		\hline\hline\hspace{4pt}
		\stepcounter{questionSec}
	}{\hline\end{longtable}\vspace{11pt}}
}{}

\renewcommand\baselinestretch{1.2}
