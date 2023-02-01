# miniproject1 - CS7637
The program is building an agent to solve the following problem: 
A farmer has to move sheep and wolves across a river using a boat.
The boat can only carry at most two animals at a time and it cannot move without at least one animal on board.
The farmer wants to ensure that no more wolves than sheep are left on either side of the river at any time.
The goal is to move all the sheep and wolves across the river safely.



\documentclass[
	%a4paper, % Use A4 paper size
	letterpaper, % Use US letter paper size
]{jdf}

\addbibresource{references.bib}

\author{Apurva Gandhi}
\email{agandhi301@gatech.edu}
\title{CS6750: Assignment M1 }

\begin{document}
%\lsstyle

\maketitle
\begin{abstract}
Throughout this project, I will investigate and design a mobile application that connects local home chefs with customers. The application's interface will allow customers to order homemade food cooked by home chefs in their neighborhood, while chefs will be able to list their food items for sale. To understand the user interface and improve the user experience, I will study existing interfaces of similar apps, such as
	\href{https://www.tiffineatz.com/Home.html}{TiffinEatz},
	\href{https://homevyte.com/}{Homevyte}, and
	\href{https://www.dishdivvy.com/} {DishDivy}My focus throughout this project will be on two specific tasks: ordering food items from a customer's perspective and listing food items from a chef's perspective. I am assuming the problem space to be a comfortable environment for novice users who are not familiar with app functionality.
\end{abstract}
\section{Problem Space}
The problem space for the two tasks of ordering food items and listing food items can be anywhere, such as while watching TV, driving a car, or discussing food with friends or family. However, the problem space is not the primary focus of this project, as it does not impact the redesign of the interface. For the purpose of this project, the problem space will be assumed to be at home or in an environment with minimal distractions. The assumption is that the user can order or list an item without interruption. For the ordering aspect of the project, the focus will be on individuals who live alone, away from home, and are busy with daily activities like work or school. This segment may include college students and working professionals who live out of state or country. For the listing aspect of the project, the focus will be on individuals who enjoy cooking, are likely in their 30s or 40s, and can prepare unique and authentic meals in their daily life. This segment may include retired mothers or housewives who care for students or working professionals. The explicit needs are straightforward, such as ordering or listing food, but the implicit needs for customers are access to home-style meals and for chefs, it is earning an income.
\section{User Types}
For the purpose of this project, the assumed user type is someone who is novice at technology usability. Since the target segment is older or retired individuals, it is assumed that their understanding of modern apps is limited. Although they may know how an app works, it is important to provide ways for them to perform intended tasks with limited app knowledge. The customer segment of the investigation may have users who are more familiar with apps, but it is still assumed that both customers and chefs have only basic knowledge of app usage and are not tech-savvy. An initial review of existing apps and platforms showed that the customer and chef populations are diverse, with a majority being Hispanic and Indian. Therefore, the user type can also be narrowed down to immigrant and/or diverse populations.
\section{Needfinding Plan 1: Surveys}
Out of all the needfinding methods covered in this course, surveys will work best for the purpose of this project. Surveys are powerful and offer many benefits for needfinding, such as the ability to investigate participants' thoughts, the collection of large amounts of user data at a low cost, and the fact that they do not require synchronous participation. However, designing surveys requires a thorough process, review, and reflection of the questions and subject matter.
\subsection{Designing Surveys}
Five tips for effective survey design are: keep it simple, consider bias, link it to your data inventory, test it, and make revisions. Writing strong survey questions is crucial to success. Good questions are clear, concise, specific, expressive, unbiased, and usable. I plan to design two surveys, one for customers and one for chefs, and send them to appropriate individuals from a list obtained from a Facebook group. This group includes customers who already purchase items through the group's posts and chefs who may be interested in participating. I will also send the surveys to friends and family to gather additional information about the design and product. 
\subsection{Possible questions}
Here are a few examples of questions that can be asked in a survey to understand and investigate existing app interfaces:



Question 1: This exemplifies how to ask clear survey question. 
From 1 to 5, rate your satisfaction with ordering an item on this app.
\item
1 - Highly dissatisfied 
2 - Dissatisfied
3 - Neutral 
4- Satisfied
5 - Highly satisfied

Question 2: It is important to not overlap ranges in questions like this. How many times per week do you order food from home made food app?
\item
A: 0-2
B: 3-5
C: 6-10
D: 11-15
E: 16+

Question 3: Asking clean and concise questions will provide better user response to this survey. How easy was to order an item from the app?
\item
A: Very easy
B: Somewhat easy
C: Not easy at all


Question 4: How satisfied were you with how quickly the interface responded to your commands?
\item
1 - Highly dissatisfied 
2 - Dissatisfied
3 - Neutral 
4- Satisfied
5 - Highly satisfied
\subsection{Data Inventory}
Generally, every part of the need-finding exercise should address an item in the data inventory. In this need-finding exercise, I plan to address the data inventory of users' tasks and sub-tasks. My goal is to understand the process users go through to complete the main task of ordering an item, including the sub-tasks they perform to reach the final checkout screen. Additionally, I aim to understand users' goals. Finally, by asking questions about their demographics and usage, I hope to learn who the users of this interface are.
\subsection{Potential Biases}
It is important to avoid biases in survey questions to ensure valid and reliable results. To do this, I will order questions logically and consistently to avoid order bias. I will also avoid respondent fatigue by limiting the number of questions and avoiding overly complex questions. This will help ensure the quality of responses. Additionally, I will avoid double-barreled questions by breaking them into separate, clear, and concise questions.

\section{Needfinding Plan 2: Interviews}
nterviews will allow me to investigate participants' thoughts. For this needfinding exercise, I plan to ask 2-3 users from each of the customer and chef groups about their experiences and tasks to achieve their desired goals. Before conducting an actual interview, I will prepare, organize, and practice with my family or friends. During the interview, I will make sure to listen actively to the participants' thoughts and let them do most of the talking. I will also be aware of my own biases and make sure to ask open-ended questions. To ask effective questions in the interview, I will focus on the six Ws: who, what, when, where, why, and how.


\item How often do you use the app to purchase homemade food?
\item What task, if any, do you find challenging when using the app?
\item Which device do you use when ordering food through the app?
\item Who do you contact if there is a cancellation or delay in delivery when using the homemade food app?
\item At what time do you typically use the app?
\item Where do you prepare your food for sale?
\item How much do you charge for your items?

\subsection{Data Inventory}
With this needfinding exercise, I aim to address the data inventory questions regarding the context of the task and the user's goals. These questions are important to understand through interviews as they may provide more open-ended responses compared to surveys. The focus of this exercise will be to answer these two inventory questions.
\subsection{Potential Biases}
One potential bias I may encounter is confirmation bias. To limit this, I will use neutral language and avoid asking leading questions. I will also avoid questions that steer respondents towards a specific answer. Additionally, I need to be aware of the Halo effect, where a positive impression of one attribute may influence the perception of other attributes. To limit these biases, I will have a structured interview process with standardized questions.

\section{Needfinding Plan 3: Evaluation of existing user interfaces}
For this needfinding exercise, I will evaluate the efficiency, accuracy, reliability, memorability, and satisfaction of three interfaces:	\href{https://www.tiffineatz.com/Home.html}{TiffinEatz},
	\href{https://homevyte.com/}{Homevyte}, and
	\href{https://www.dishdivvy.com/} {DishDivy}.
I will find them in the App Store and conduct a qualitative evaluation, as qualitative data is useful in improving interfaces. The focus of the evaluation will be on the overall experience of the user. I will ask questions such as, "What did you like/dislike?" "What were you thinking while using this interface?" "What was your goal when taking a particular action?" I will prefer live demonstrations to capture qualitative evaluation and take notes and/or record videos for analysis. To maximize the benefits of this evaluation, I will conduct pilot studies, focus on feedback, use clear questions, instruct users on what to do, not how, and capture their satisfaction. The results of this evaluation will inform ongoing design decisions, provide insights into the participants' thought process, and draw conclusions from actual users.
\subsection{Data Inventory}
The data inventory can be used to gain insights into the current state of the user interface, identify areas for improvement, and inform design decisions for future iterations. I will address the reasons for using the user interface, the actions performed, and the outcomes desired. Furthermore, users' qualitative and quantitative comments on the user interface and information on how they interact with the interface (such as mouse clicks, keyboard inputs, scrolling, etc.) will provide insight into understanding the interface and how it can be improved. As part of the data inventory for this exercise, I will make records of any errors or issues users have experienced while using the interface and compare the user interface with similar products in the market, including their strengths and weaknesses.
\subsection{Potential Biases}
One potential bias in evaluating existing user interfaces is anchoring bias. The evaluator may be influenced by the first impression they have of the interface, shaping their overall evaluation. To minimize its impact, I would gather data from multiple sources, such as user feedback, analytics, and heuristic evaluations. I would also involve multiple evaluators to reduce the influence of any one person's bias. Furthermore, I would ensure diversity among the evaluation team to bring in different perspectives, as different backgrounds and skill sets may result in different evaluations. It is important to be aware of and recognize unconscious biases.
\end{document}
