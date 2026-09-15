% ==========================================
% INTRODUCTION
% ==========================================

% ------------------------------------------
% Family Tree Database (Facts)
% ------------------------------------------

% Gender - Different Generations
male(avraham). male(yitzhak). male(moshe). male(yaakov). male(david). male(yonatan). male(reuven). male(dan).
female(sara). female(rivka). female(rachel). female(dina). female(lea). female(tamar). female(noa).

% Married Couples
% Assumption: married(Male, Female)
married(avraham, sara).
married(yitzhak, rivka).
married(moshe, rachel).
married(yaakov, lea).
married(yonatan, tamar).

% Parenting Relations
% Assumprion: parent(Parent, Child)
% 1st gen to 2nd gen:
parent(avraham, yitzhak). parent(sara, yitzhak).
parent(avraham, rachel).  parent(sara, rachel).
% 2nd gen to 3rd gen:
parent(yitzhak, yaakov).  parent(rivka, yaakov).
parent(yitzhak, dina).    parent(rivka, dina).
parent(yitzhak, david).   parent(rivka, david).
parent(moshe, yonatan).   parent(rachel, yonatan).
% 3rd gen to 4th gen:
parent(yaakov, reuven).   parent(lea, reuven).
parent(yaakov, noa).      parent(lea, noa).
parent(yonatan, dan).     parent(tamar, dan).

% ------------------------------------------
% The 14 Family Relation Definitions (Paradicts)
% ------------------------------------------
% 1. Father
father(F, C) :- 
    male(F), 
    parent(F, C).
% 2. mother
mother(M, C) :- 
    female(M), 
    parent(M, C).
% 3. Son
son(S, P) :- 
    male(S), 
    parent(P, S).
% 4. Daughter
daughter(D, P) :- 
    female(D), 
    parent(P, D).
% 5. Grandfather
grandfather(GF, GC) :- 
    father(GF, P), 
    parent(P, GC).
% 6. Grandmother
grandmother(GM, GC) :- 
    mother(GM, P), 
    parent(P, GC).
% 7. Grandson
grandson(GS, GP) :- 
    male(GS), 
    parent(GP, P), 
    parent(P, GS).
% 8. Granddaughter
granddaughter(GD, GP) :- 
    female(GD), 
    parent(GP, P), 
    parent(P, GD).
% 9. Sibling
% To prevent duplications - demand both to have the same father and the same mother
sibling(X, Y) :- 
    father(F, X), father(F, Y), 
    mother(M, X), mother(M, Y), 
    X \= Y.
% 10. Uncle of NO Blood Relation (the mate of an uncle by blood)
uncle_by_marriage(U, N) :- 
    male(U), 
    married(U, Aunt), 
    female(Aunt), 
    sibling(Aunt, P), 
    parent(P, N).

% 11. Son of Female Aunt
cousin_son_of_aunt(C, Person) :- 
    male(C), 
    mother(Aunt, C), 
    sibling(Aunt, P), 
    parent(P, Person).
% 12. Brother in Law
brother_in_law(BIL, Person) :- 
    male(BIL),
    (
        (married(BIL, Sister), sibling(Sister, Person)) ;
        (sibling(BIL, Spouse), married(Person, Spouse)) ;
        (sibling(BIL, Spouse), married(Spouse, Person))
    ).
% 13. Female Niece
niece(N, Person) :- 
    female(N), 
    parent(Sibling, N), 
    sibling(Sibling, Person).
% 14-sub. Cousins of First Degree
first_cousin(C1, C2) :- 
    parent(P1, C1), 
    parent(P2, C2), 
    sibling(P1, P2).
% 14. Cousins of Second Degree
second_cousin(X, Y) :- 
    parent(PX, X), 
    parent(PY, Y), 
    first_cousin(PX, PY).


% ==========================================
% Recursion and Lists
% ==========================================

% 1. reverse(L, Z)
% Reverses the elements of list L and unifies the result with Z.
reverse(L, Z) :- 
    reverse_acc(L, [], Z).

% Helper predicate for reverse/2
reverse_acc([], Acc, Acc).
reverse_acc([H|T], Acc, Z) :- 
    reverse_acc(T, [H|Acc], Z).


% 2. member(X, L)
% Checks if X is an element present in list L.
member(X, [X|_]).
member(X, [_|T]) :- 
    member(X, T).


% 3. palindrome(L)
% Checks if a list reads the same forwards and backwards.
palindrome(L) :- 
    reverse(L, L).


% 4. sorted(L)
% Returns true if L is sorted in non-descending order, false otherwise.
sorted([]).               % Base case: An empty list is inherently sorted.
sorted([_]).              % Base case: A list with a single element is sorted.
sorted([X, Y | T]) :-     % Recursive step: Check the first two elements.
    X =< Y,               % The first element must be less than or equal to the second.
    sorted([Y | T]).      % Recursively check the rest of the list.


% 5. permutation(L, P)
% Generates a permutation P of the list L. 

% Helper predicate to extract an element from a list.
% remove_element(Element, List, RestOfList)
remove_element(X, [X|T], T).
remove_element(X, [H|T], [H|R]) :- 
    remove_element(X, T, R).

% The permutation logic
permutation([], []).
permutation(L, [H|T]) :- 
    remove_element(H, L, Rest), % Non-deterministically pick an element H from L.
    permutation(Rest, T).       % Recursively find a permutation for the remaining elements.


% ==========================================
% Arithmetics
% ==========================================

% ------------------------------------------
% Question 1
% ------------------------------------------

% 1.a. scum(N, Res)
% Calculates the sum of numbers from 1 to N (where N >= 1) and stores it in Res.
scum(1, 1).
scum(N, Res) :- 
    N > 1, 
    Prev is N - 1, 
    scum(Prev, PrevRes), 
    Res is PrevRes + N.

% 1.b. sumDigits(Num, Sum)
% Sums the digits of Num (where Num >= 0) and stores the result in Sum.
sumDigits(0, 0).
sumDigits(Num, Sum) :- 
    Num > 0, 
    Digit is Num mod 10, 
    Rest is Num // 10, 
    sumDigits(Rest, RestSum), 
    Sum is RestSum + Digit.

% ------------------------------------------
% Question 2
% ------------------------------------------

% 2.a. split(N, Res)
% Splits N (where N >= 0) into a list of its digits in Res.
% Uses a helper predicate with an accumulator to extract digits correctly.
split(0, [0]).
split(N, Res) :- 
    N > 0, 
    split_acc(N, [], Res).

split_acc(0, Acc, Acc).
split_acc(N, Acc, Res) :- 
    N > 0, 
    Digit is N mod 10, 
    Rest is N // 10, 
    split_acc(Rest, [Digit|Acc], Res).

% 2.b. create(List, N)
% Takes a list of digits and creates a number N where the leftmost element 
% is the units digit, the second is tens, etc.
% e.g., create([1,2,3,4], N) -> N = 4321.
create(List, N) :- 
    create_helper(List, 1, 0, N).

% Helper for create/2: Multiplier tracks powers of 10 (1, 10, 100...)
create_helper([], _Multiplier, Acc, Acc).
create_helper([H|T], Multiplier, Acc, N) :- 
    NewAcc is Acc + H * Multiplier, 
    NewMultiplier is Multiplier * 10, 
    create_helper(T, NewMultiplier, NewAcc, N).

% 2.c. reverse_number(N, NewN)
% Receives a number N and returns a new number NewN with reversed digits.
% Uses split/2 and create/2.
reverse_number(N, NewN) :- 
    split(N, List), 
    create(List, NewN).

% ------------------------------------------
% Question 3
% These predicates rely on member/2 (which was defined earlier).
% ------------------------------------------

% 3.a. intersection(L1, L2, Z)
% Z is the intersection of lists L1 and L2 (elements present in both).
intersection([], _, []).
intersection([H|T], L2, [H|Z]) :- 
    member(H, L2), 
    intersection(T, L2, Z).
intersection([H|T], L2, Z) :- 
    \+ member(H, L2), 
    intersection(T, L2, Z).

% 3.b. minus(L1, L2, Z)
% Z is the subtraction of L2 from L1 (elements in L1 that are NOT in L2).
minus([], _, []).
minus([H|T], L2, [H|Z]) :- 
    \+ member(H, L2), 
    minus(T, L2, Z).
minus([H|T], L2, Z) :- 
    member(H, L2), 
    minus(T, L2, Z).