{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red254\green213\blue177;\red42\green45\blue49;\red201\green201\blue201;
\red184\green93\blue213;\red81\green156\blue233;\red136\green185\blue102;\red72\green168\blue181;\red203\green203\blue203;
}
{\*\expandedcolortbl;;\cssrgb\c100000\c86667\c74510;\cssrgb\c21961\c23137\c25098;\cssrgb\c82745\c82745\c82745;
\cssrgb\c77647\c47059\c86667;\cssrgb\c38039\c68235\c93333;\cssrgb\c59608\c76471\c47451;\cssrgb\c33725\c71373\c76078;\cssrgb\c83529\c83529\c83529;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl400\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # Program make a simple calculator\cf4 \strokec4 \
\
\cf2 \strokec2 # This function adds two numbers\cf4 \strokec4 \
\pard\pardeftab720\sl400\partightenfactor0
\cf5 \strokec5 def\cf4 \strokec4  \cf6 \strokec6 add\cf4 \strokec4 (x, y):\
    \cf5 \strokec5 return\cf4 \strokec4  x + y\
\
\pard\pardeftab720\sl400\partightenfactor0
\cf2 \strokec2 # This function subtracts two numbers\cf4 \strokec4 \
\pard\pardeftab720\sl400\partightenfactor0
\cf5 \strokec5 def\cf4 \strokec4  \cf6 \strokec6 subtract\cf4 \strokec4 (x, y):\
    \cf5 \strokec5 return\cf4 \strokec4  x - y\
\
\pard\pardeftab720\sl400\partightenfactor0
\cf2 \strokec2 # This function multiplies two numbers\cf4 \strokec4 \
\pard\pardeftab720\sl400\partightenfactor0
\cf5 \strokec5 def\cf4 \strokec4  \cf6 \strokec6 multiply\cf4 \strokec4 (x, y):\
    \cf5 \strokec5 return\cf4 \strokec4  x * y\
\
\pard\pardeftab720\sl400\partightenfactor0
\cf2 \strokec2 # This function divides two numbers\cf4 \strokec4 \
\pard\pardeftab720\sl400\partightenfactor0
\cf5 \strokec5 def\cf4 \strokec4  \cf6 \strokec6 divide\cf4 \strokec4 (x, y):\
    \cf5 \strokec5 return\cf4 \strokec4  x / y\
\
\
\cf5 \strokec5 print\cf4 \strokec4 (\cf7 \strokec7 "Select operation."\cf4 \strokec4 )\
\cf5 \strokec5 print\cf4 \strokec4 (\cf7 \strokec7 "1.Add"\cf4 \strokec4 )\
\cf5 \strokec5 print\cf4 \strokec4 (\cf7 \strokec7 "2.Subtract"\cf4 \strokec4 )\
\cf5 \strokec5 print\cf4 \strokec4 (\cf7 \strokec7 "3.Multiply"\cf4 \strokec4 )\
\cf5 \strokec5 print\cf4 \strokec4 (\cf7 \strokec7 "4.Divide"\cf4 \strokec4 )\
\
\cf5 \strokec5 while\cf4 \strokec4  \cf8 \strokec8 True\cf4 \strokec4 :\
    \cf2 \strokec2 # take input from the user\cf4 \strokec4 \
    choice = \cf5 \strokec5 input\cf4 \strokec4 (\cf7 \strokec7 "Enter choice(1/2/3/4): "\cf4 \strokec4 )\
\
    \cf2 \strokec2 # check if choice is one of the four options\cf4 \strokec4 \
    \cf5 \strokec5 if\cf4 \strokec4  choice \cf5 \strokec5 in\cf4 \strokec4  (\cf7 \strokec7 '1'\cf4 \strokec4 , \cf7 \strokec7 '2'\cf4 \strokec4 , \cf7 \strokec7 '3'\cf4 \strokec4 , \cf7 \strokec7 '4'\cf4 \strokec4 ):\
        num1 = float(\cf5 \strokec5 input\cf4 \strokec4 (\cf7 \strokec7 "Enter first number: "\cf4 \strokec4 ))\
        num2 = float(\cf5 \strokec5 input\cf4 \strokec4 (\cf7 \strokec7 "Enter second number: "\cf4 \strokec4 ))\
\
        \cf5 \strokec5 if\cf4 \strokec4  choice == \cf7 \strokec7 '1'\cf4 \strokec4 :\
            \cf5 \strokec5 print\cf4 \strokec4 (num1, \cf7 \strokec7 "+"\cf4 \strokec4 , num2, \cf7 \strokec7 "="\cf4 \strokec4 , add(num1, num2))\
\
        \cf5 \strokec5 elif\cf4 \strokec4  choice == \cf7 \strokec7 '2'\cf4 \strokec4 :\
            \cf5 \strokec5 print\cf4 \strokec4 (num1, \cf7 \strokec7 "-"\cf4 \strokec4 , num2, \cf7 \strokec7 "="\cf4 \strokec4 , subtract(num1, num2))\
\
        \cf5 \strokec5 elif\cf4 \strokec4  choice == \cf7 \strokec7 '3'\cf4 \strokec4 :\
            \cf5 \strokec5 print\cf4 \strokec4 (num1, \cf7 \strokec7 "*"\cf4 \strokec4 , num2, \cf7 \strokec7 "="\cf4 \strokec4 , multiply(num1, num2))\
\
        \cf5 \strokec5 elif\cf4 \strokec4  choice == \cf7 \strokec7 '4'\cf4 \strokec4 :\
            \cf5 \strokec5 print\cf4 \strokec4 (num1, \cf7 \strokec7 "/"\cf4 \strokec4 , num2, \cf7 \strokec7 "="\cf4 \strokec4 , divide(num1, num2))\
        \
        \cf2 \strokec2 # check if user wants another calculation\cf4 \strokec4 \
        \cf2 \strokec2 # break the while loop if answer is no\cf4 \strokec4 \
        next_calculation = \cf5 \strokec5 input\cf4 \strokec4 (\cf7 \strokec7 "Let's do next calculation? (yes/no): "\cf4 \strokec4 )\
        \cf5 \strokec5 if\cf4 \strokec4  next_calculation == \cf7 \strokec7 "no"\cf4 \strokec4 :\
          \cf5 \strokec5 break\cf4 \strokec4 \
    \
    \cf5 \strokec5 else\cf4 \strokec4 :\
        \cf5 \strokec5 print\cf4 \strokec4 (\cf7 \strokec7 "Invalid Input"\cf4 \strokec4 )\cf9 \strokec9 \
}