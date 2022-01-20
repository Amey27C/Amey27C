%  An Englishman (Mr. Salmon), a Welshman (Mr. Green), and a Scotsman (Mr. Brown) met for lunch one day. 
%  One man was wearing a salmon tie, another was wearing a green tie and the third was wearing a brown tie. "Isn't it funny," said Mr. Brown to the others, 
%  "that not one of us is wearing a tie which matches our name?" "That's true," agreed the man wearing the green tie. Can you now say what color tie each man was wearing?

%  Answer Set Programming was used as a declarative approach to creating stable models. 

%Reference - stated the facts and rules practiced in the exercises of lab 2

statement_by(brown).
% Mr Brown made a statement that none of them were wearing same ties which matched their names .

uttered_by(green).                   				
% which has an utterance by the person wearing a green tie.

person(brown).
person(green).
person(salmon).

% Fact :- There are 3 people named - 1. Mr Brown.                      			
%                                  - 2. Mr Green.                     			
%                                  - 3. Mr Salmon. 

tie(brown).
tie(green).
tie(salmon).
% Fact :- There are 3 coloured ties - 1. Brown.                                        
% 			            - 2. Green.						                
% 			            - 3. Salmon.

1{wearing(P,T) : person(P)}1 :- tie(T).             % Only one person per tie.

1{wearing(P,T) : tie(T)}1 :- person(P).             % Only one tie per person. 

:- wearing(P,T) , P==T.                             
% It states that Mr Brown and the person wearing a green tie cannot be the same entities.

:- wearing(P,T): statement_by(P), uttered_by(T).
