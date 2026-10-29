# Phone Numbers: Clean, Validate, Parse

**Time:** 60 minutes · **Type:** retrieval + enrichment

## The patterns (come back to this table all phase)

Every string and loop problem you'll see, on the GCF or at work, is built from a few patterns. Each one is defined by **what you keep track of**. Learn the real function first; it's how you'll remember the pattern.

| #   | Pattern | What you keep track of | Real function | Example | GCF cousin | Today |
| --- | ------- | ---------------------- | ------------- | ------- | ---------- | ----- |
| 1   | Build a new string | a result that grows | `normalize_phone` (every sign-up form) | `"(718) 555-0142"` → `"7185550142"` | digit filters, reverseVowels | ✅ Clean |
| 2   | Pull parts by position | fixed positions | `format_phone` (every contact card) | `"7185550142"` → `"(718) 555-0142"` | reverseDigitsInPairs | ✅ Parse |
| 3   | Any / all | a yes/no, answered "no" early | `is_valid_phone` (form validation) | `"718-555-0142 cell"` → `False` | validity checks | ✅ Validate |
| 4   | Count | a counter | `count_mentions` (group chats) | `"@ana can you and @bo cover Friday?"` → `2` | countOccurrences650 | |
| 5   | Best so far | the best value seen | `earliest` (transit apps) | `["08:40", "07:55", "09:10"]` → `"07:55"` | max / min problems | |
| 6   | Compare to neighbor | the previous item | `collapse_spaces` (text cleanup) | `"Running    late,  sorry"` → `"Running late, sorry"` | brokenKeyboard2-700 | |
| 7   | Two positions | two indexes | `merge_schedules` (calendars) | `["09:00", "13:00"]` + `["10:30", "15:00"]` → `["09:00", "10:30", "13:00", "15:00"]` | reverseVowels, merging sorted arrays | |
| 8   | Tally | a dict of counts | `poll_results` (group-chat polls) | `["pizza", "tacos", "pizza"]` → `{"pizza": 2, "tacos": 1}` | firstNotRepeatingCharacter, createAnagram | ✅ Sign-up list |
| 9   | Fixed window | a slice that slides | rolling step totals (fitness apps) | `[4000, 6000, 5000, 9000]`, 3 days → `[15000, 20000]` | maxSumSubarray | |

Most GCF Q1 and Q2 problems combine two of these.

**Files in this repo**

| File | Used in |
| ---- | ------- |
| `clean.py` | Warm-up, Part 1 |
| `validate.py` | Part 2 |
| `parse.py` | Part 3 |
| `signups.py` | Part 4 |
| `zip_code.py` | Independent check |

Each file includes working versions of the earlier steps, so you can start any part even if you didn't finish the one before.

## How this activity works

Today starts with what you already know, pulled from memory, then stretches it. Wrong predictions are expected. They show you exactly which idea to look at next.

### When you're stuck

Raise your hand when either of these is true:

- You've been stuck on one step for **5 minutes**, or
- You've tried **two different things** and neither worked.

Look for the 🙋 symbol in this guide. It marks the places where fellows most often get stuck, and asking for help there is the right move.

**When you ask for help, come with:**

1. The line of code you're stuck on
2. What you predicted
3. What actually happened
4. What you've tried so far

The ✅ symbol marks a checkpoint where you show an instructor your work before moving on.

---

## The big ideas for today

| #   | Idea | Try it in the REPL |
| --- | ---- | ------------------ |
| 1   | Clean before you compare. The same number arrives in many formats. Turn each one into one form first, or one person looks like two. | `"(718) 555-0142" == "718.555.0142"` |
| 2   | Each side of `or` is its own check. A side with no comparison is judged alone, and any non-empty text counts as true. | `d = "7"`, `d == "0" or "1"`, `d in "01"` |
| 3   | Answer "no" inside the loop, as soon as you find a problem. Answer "yes" only after the loop has checked everything. | Part 2 |
| 4   | Each position in a string holds one character, and a slice pulls out a run of them. Parsing means giving those runs names. | `digits = "7185550142"`, `digits[0:3]`, `digits[6:]` |
| 5   | A dict can count: one key per cleaned value, and its count grows each time that value shows up again. | `counts = {}`, `counts["718"] = counts.get("718", 0) + 1`, `counts` |
| 6   | One passing test doesn't prove a function is right. Try the strange cases: empty text, a country code, a typed word, the letter O instead of a zero. | Every part |

## Habits for today

**Coding habit:** Clean, validate, and parse are separate functions, and each one is tested alone before you combine them. When a character has to match one of several values, use one `in` check, not an `or` chain.

**Working habit: Plan before coding (PEDAC, step 1).**

- **Hold on. Before I type: what goes in, and what comes out?** Every file has an `# In:` and `# Out:` line. Fill it in before you write code. Say where each input comes from (typed, a parameter, already in the code) and where each output goes (printed or returned).
- Tell your partner your In/Out, then start. If theirs is different, you've found a question to sort out before either of you writes code.

---

## Warm-up: Retrieval (8 minutes, no notes)

Open `clean.py`. Fill in `# In:` and `# Out:`, then write `normalize_phone` **from memory**. Don't look anything up. Pulling it from memory is the practice.

Run `python3 clean.py`. All four warm-up tests should match their expected values.

🙋 **Ask for help if:** after 5 minutes you can't remember how to keep only the digits. Look at pattern 1 in the table, then try again.

---

## Part 1: Clean, the strange case (6 minutes)

People type their country code. Uncomment the first Part 1 test. **Before you change anything**, predict what your function returns for `"+1 (718) 555-0142"` and write it in the `# Prediction` comment. Run it.

Now add the country-code rule from the spec at the top of the file. Uncomment the other two tests and run.

Self-check: all three Part 1 tests should match. `"212-555-01"` should still give back `21255501`. Cleaning doesn't decide what's valid; that's the next step's job.

---

## Part 2: Validate (13 minutes)

### 2a. Code review: predict and run

Open `validate.py`. A teammate wrote two helpers. Each test has a comment with the value it *should* give back. **Don't run it yet.** Predict what each line will actually print and write your predictions in the comments.

Run `python3 validate.py` and fill in each `# Actual:` line. Then write one sentence per helper explaining what's wrong. Use big ideas 2 and 3.

**Swap with a partner** and compare explanations.

🙋 **Ask for help if:** you and your partner can't agree on why `only_phone_chars("")` prints `None`.

### 2b. Fix the helpers

Fix `only_phone_chars` and `area_code_ok`. Change only what's needed.

Self-check: run it. All six test lines should now match their expected values.

### 2c. Write the validator

Fill in `# In:` and `# Out:`, then write `is_valid_phone(raw)` using `normalize_phone` and your two fixed helpers. Uncomment the six tests.

Self-check: all six tests match. Then answer as a comment: why does `"718-555-0142 cell"` need the character check, when cleaning would turn it into 10 good digits?

✅ **Checkpoint:** Show an instructor your fixed helpers and tell them, in one sentence each, what the two bugs were.

---

## Part 3: Parse (7 minutes)

Open `parse.py`. The input is already clean and valid. Write `format_phone` and `parse_phone` using slices (big idea 4).

Self-check: both test lines print exactly their expected values, including the space after `)`.

---

## Part 4: The sign-up list (11 minutes)

Open `signups.py` and read the docstring: a food pantry's text-alert sign-up list, with people who signed up twice and entries that aren't phone numbers.

Fill in `# In:` and `# Out:`. Before you code, look at the list and predict by hand: how many different people signed up?

**Requirements**

1. `signup_report(entries)` gives back a dict of counts and a list of invalid entries.
2. Use the working `is_valid_phone` and `normalize_phone` in the file. Don't rewrite them.
3. Count with a dict, keyed by the **clean** number (big idea 5).
4. After the function, print the formatted numbers that signed up more than once, and the number of different people.
5. The program must run without crashing.

**Check your output:**

```
{'7185550142': 2, '3475550199': 2, '9295550100': 1}
['212-555-01', '718-555-O142']
Signed up twice: ['(718) 555-0142', '(347) 555-0199']
People: 3
```

If your dict has five or more keys, reread big idea 1: what are you using as the key?

🙋 **Ask for help if:** your counts are all `1` and you can't tell why.

✅ **Checkpoint:** Show an instructor your output, and point to which pattern from the table each part of your code uses.

---

## Part 5: Independent check (10 minutes)

Your instructor will hand this out. Work alone, with no AI and no notes, and write your prediction on paper before you run anything.

---

## Going further (optional)

Use one new tool, `set()`. A set keeps only one copy of each value.

1. In the REPL, try `len(set(["7185550142", "7185550142", "3475550199"]))`.
2. In `signups.py`, count the number of different people in one line, using a set of the clean, valid numbers. It should match `People: 3`.
3. What can your dict tell you that the set can't?
