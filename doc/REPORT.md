The first thing I did was to have an understanding of what the project was supposed to be, 
so I read the documentation and made myself familiar with the rules and the general game flow. 
This method helped because doing this made me understood what the requirements were, 
and it also made it easier to identify errors afterwards.

After this, I ran the main module just to see if the program works and it turns out that it didn't. 
This was easy to fix because the terminal provides all of the error messages 
i.e. SyntaxError, TypeError, especially what line and file the error occurred on. 
I fixed three errors before I could run the game and test the game loop. 
My first strategy was this, to run the game without knowing how features were implemented. 
Doing this, I identified many bugs without the awareness of the different objects in the whole project. 

Although non-exhaustive, the test suite was very useful in identifying errors 
that couldn't be found with black-box testing. This was my second strategy, 
white-box testing via unit testing method. It is highly effective because it 
allows me to test the implementation of the different objects in the project, 
and together with tools like breakpoints, watch, and the different step methods, 
I could see how a specific 'unit' works during runtime. I fixed every failing 
test case because they all provided their error messages and made debugging easier. 
The fact that I was always looking at the documentation also helped massively 
since I knew what the expected behaviour should be.

My strategy for improving the codebase was to divide the task into two parts: 
improving documentation, inline or otherwise, and improving the actual code 
which included inefficiencies, additional test cases, and readability. 
At this point, I had a clear understanding of the current codebase so 
I wrote additional comments and docstrings for the program. 
I also added test cases for user_interface and cards files. 
Since I wasn't familiar with testing yet so I couldn't follow a 
full test-driven development and I noticed how it would have benefitted me if I wrote additional test cases first.

To summarise my whole strategy, reading the documentation was my first 
step into familiarising myself with the requirements. Black box testing was the next. 
Bugs during runtime are very easy to identify. White box testing with unit testing 
while keeping track of the different requirements was my main strategy to fully debug the game. 
I must admit that there were extra bugs that couldn't be identified using this method and 
required more intricate reading of the codebase. I then tried to improve the codebase by 
writing tests, developing the documentation and improving the actual code itself. 
The tools I used: the debugger, interpreter, testing module, and IDE all helped 
in recognising all of the 15 bugs that existed in the project.