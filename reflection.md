# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - hints were backwards (saying to go lower when the secret was higher than the guess)
  - allowed numbers outside of 1-100 and still provided hints (go lower for a negative number guess)

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
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
