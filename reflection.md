# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - When I entered a number, it gave a hint saying go higher or go lower. Each number entered in subsequent 
  guesses sometimes changed the attempts number, other times not. After the first game ended, it became 
  clear that there were errors as the game did not work as intended.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - provided hints were backwards (saying to go lower when the secret was higher than the guess)
  - the game allowed numbers outside of 1-100 and still provided hints (go lower for a negative number guess)

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|guess of -2 | error | "go lower" | "none" |
|first guess of 50 | attempt count to go down | no change ("Attempts left: 8") |"none"|
|guess of 10 when secret is 8| "go lower" | "go higher" | "none"|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
   - used Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
   - I asked it about the function "check_guess" and it found a lot of things wrong
   - It noted the duplicate check for equality and flagged the ambiguous type change in the exception handler 
   - I verified the result by asking AI to investigate where "secret" was generated and what the expected or possible variable types would be. It found that it was being generated in app.py line 159-161 as an int and getting converted into a string for even attempts while being a int for odd attempts. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
   - AI noted incorrect "too low" logic, but it was flagging that the if statement was only explicitly checking if guess > secret and letting else pick up the "guess < secret" case. This was actually fine because the equality is checked before the exception handler.
   - The AI suggested explicit if conditionals, so if g > s, elif g < s, else "win". This would work but does not address the actually text being wrong for the hint e.g. guess was too high, return "Too High" and should tell user to go lower.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I checked through the app with the inputs to get the correct outcome. Then I backchecked the logic of the code, asking the AI follow ups if anything is unclear. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - I reviewed the pytest logic of the new cases that the AI generated and agreed with the outcome. It was my first time using pytest and I had to make adjustments to the prewritten tests because we changed the check_guess function. 
  - One specific example is with the parse_guess tests for input validation. I didn't realize that the number guess could be a decimal until I read through the tests and saw that it was checking if a decimal number in range would pass. This is ultimately a human decision but it was an interesting edge case I didn't catch previously.
- Did AI help you design or understand any tests? How?
  - AI helped me design 4 new tests for the high/low bug and string/int type bug. It checked that the hints were correct and that any input strings were changed and generated the right answer.
  - AI also helped me understand why 100.5 was being accepted as in an input due to the int conversion prior to the range check. It wrote a couple test cases for the input validation, one of which said 100.5 should fail. So the test failed, but then AI got confused and thought the test was wrong not the logic. I corrected this and got the logic updated in parse_guess.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Streamlit reruns essentially resets the code execution/inputs/outputs. You can call it to reset the state of the app basically. 
  - Session state is how streamlit is tracking info between sessions (info persists even if the app reruns)

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    - It was easy to use AI to generate the commit comments, so I might do that again in the future. 
- What is one thing you would do differently next time you work with AI on a coding task?
  - I would tell it to explain what it is doing before letting it generate. It is easier to address logic issues and identify high level improvements before going through generated code.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - AI generates code only as well as directed. It doesn't actually understand intent, but it can do exactly what you want it to do with some coaching. 
