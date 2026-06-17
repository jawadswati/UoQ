# Unit 04 — Grammar concepts (17 lessons)

Unit 04 is a single, tightly-structured unit on **pronouns (ضمائر)** — both the
**detached pronouns** (ضمیرِ منفصل: هُوَ، أَنْتَ، هِيَ، أَنَا) and the **attached
pronoun suffixes** (ضمیرِ متصل: ـهُ، ـكَ، ـهَا، ـي). It then closes with two short
word-pattern lessons (سبق 17 + the مفعول feature box).

The unit drills each pronoun in a fixed four-step cycle, which makes it very systematic:

1. **detached pronoun** as a subject — هُوَ رَسُولٌ ("he is a messenger");
2. **suffix on a noun** (possessive) — بَيْتُهُ ("his house");
3. **suffix on a noun after a particle** — فِي بَيْتِهِ ("in his house");
4. **suffix fused onto a particle** — لَهُ، مِنْهُ، فِيهِ، إِلَيْهِ، عَلَيْهِ، إِنَّهُ.

This cycle is repeated for the masculine 3rd person (هُوَ/ـهُ, lessons 1–4), the masculine
2nd person (أَنْتَ/ـكَ, lessons 5–8), the feminine 3rd person (هِيَ/ـهَا, lessons 9–12),
and the 1st person (أَنَا/ـي, lessons 13–16).

Base nouns are in `vocabulary.csv` (section `noun-bases`); the fused particle+pronoun forms
are in `vocabulary.csv` (section `pronoun-on-particle`); full Quranic verses are in
`ayaat.csv`. Page flow runs right→left across spreads, and the slide images are out of page
order (slide order = pages 2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38).

## Quick reference

| # | Topic | Idea |
|---|-------|------|
| 1 | هُوَ (detached) | "he/it is …": هُوَ رَسُولٌ، هُوَ الْحَقُّ، هُوَ السَّمِيعُ الْبَصِيرُ |
| 2 | ـهُ on a noun | "his / its": بَيْتُهُ، رَبُّهُ، رَحْمَتُهُ، قَوْلُهُ |
| 3 | ـهُ after a particle | both inflect; ـهُ→ـهِ after kasra/yaa: فِي بَيْتِهِ، مِنْ رَبِّهِ، إِلَى رَحْمَتِهِ |
| 4 | ـهُ on a particle | لَهُ، مِنْهُ، فِيهِ، إِلَيْهِ، عَلَيْهِ، إِنَّهُ، أَنَّهُ |
| 5 | أَنْتَ (detached) | "you are …" (masc.): أَنْتَ يُوسُفُ، أَنْتَ رَبٌّ، أَنْتَ نَذِيرٌ |
| 6 | ـكَ on a noun | "your" (masc.): بَيْتُكَ، رَبُّكَ، رَحْمَتُكَ |
| 7 | ـكَ after a particle | فِي بَيْتِكَ، مِنْ رَبِّكَ، فِي رَحْمَتِكَ |
| 8 | ـكَ on a particle (+ عَنْ) | لَكَ، مِنْكَ، فِيكَ، إِلَيْكَ، عَلَيْكَ، عَنْكَ، إِنَّكَ; عَنْ = "about" |
| 9 | هِيَ (detached) | "she/it is …" (fem.): هِيَ فِتْنَةٌ، هِيَ ظَالِمَةٌ |
| 10 | ـهَا on a noun | "her / its" (fem.): بَيْتُهَا، رَبُّهَا، زَوْجُهَا |
| 11 | ـهَا after a particle | فِي بَيْتِهَا، مِنْ رَبِّهَا، مِنْ بَعْدِهَا |
| 12 | ـهَا on a particle | لَهَا، مِنْهَا، فِيهَا، إِلَيْهَا، عَلَيْهَا، إِنَّهَا |
| 13 | أَنَا (detached) | "I am …": أَنَا يُوسُفُ، أَنَا نَذِيرٌ، أَنَا بَشَرٌ |
| 14 | ـي on a noun | "my": بَيْتِي، رَبِّي، رَحْمَتِي، دِينِي |
| 15 | ـي after a particle | فِي بَيْتِي، مِنْ رَبِّي، عَلَى نَفْسِي |
| 16 | ـي on a particle | لِي، مِنِّي، فِيَّ، إِلَيَّ، عَلَيَّ، إِنِّي |
| 17 | مُجْرِمًا / مَفْعُول | tanwīn-alif ending = "as / being …"; مَفْعُول pattern = passive "done-to" |

---

## The big idea — ضمیر (pronoun)

A **ضمیر** stands in place of a noun. Arabic has two kinds:

- **ضمیرِ منفصل (detached / standalone)** — written as a separate word and used as the
  subject: هُوَ ("he/it"), أَنْتَ ("you", masc.), هِيَ ("she/it"), أَنَا ("I").
  هُوَ رَسُولٌ = "he is a messenger".
- **ضمیرِ متصل (attached / suffix)** — joined to the end of a word. On a **noun** it is
  possessive (بَيْتُهُ = "his house"); on a **verb** or **particle** it is the object
  ("him/it"). The four suffixes taught here are ـهُ، ـكَ، ـهَا، ـي.

## سبق 1 — هُوَ ("he / it is")
**Rule:** هُوَ = "وہ / وہ ہے". As a subject it makes a simple sentence with the predicate
that follows: هُوَ رَبٌّ، هُوَ رَسُولٌ، هُوَ شِفَاءٌ. In the Quran it very often introduces
an attribute of Allah, and is then used emphatically:
هُوَ اللهُ، هُوَ السَّمِيعُ الْبَصِيرُ، هُوَ الْعَزِيزُ الْحَكِيمُ، هُوَ الْأَوَّلُ وَهُوَ الْآخِرُ.
With a preceding ذٰلِكَ / (الـ)-word it gives a second emphasis ("he is the very …"):
هُوَ الْحَقُّ ("it is the truth").

## سبق 2 — ـهُ on a noun ("his / its")
**Rule:** adding **ـهُ** to the end of a noun gives "اس کا / اس کی".
بَيْت → بَيْتُهُ (his house), رَبّ → رَبُّهُ (his Lord), رَحْمَة → رَحْمَتُهُ (His mercy),
قَوْل → قَوْلُهُ، عَمَل → عَمَلُهُ، قَلْب → قَلْبُهُ، عَرْش → عَرْشُهُ، كُرْسِيّ → كُرْسِيُّهُ.

## سبق 3 — ـهُ on a noun after a particle
**Rule:** when a noun carrying ـهُ follows a particle (مِنْ، فِي، عَلَى، إِلَى…), **both**
inflect, and the suffix is read **ـهِ** after a kasra or a yaa:
فِي بَيْتِهِ (in his house), مِنْ رَبِّهِ (from his Lord), إِلَى رَحْمَتِهِ (to His mercy),
فِي قَلْبِهِ، فِي عُنُقِهِ، إِلَى قَوْمِهِ، بِحَمْدِهِ، بِإِذْنِهِ، بِيَمِينِهِ، لِرَبِّهِ، لِرَسُولِهِ.

## سبق 4 — ـهُ fused onto a particle
**Rule:** the same ـهُ attaches directly to the short particles to give object/relational
forms:

| particle | + ـهُ | meaning |
|----------|-------|---------|
| لِـ | لَهُ | for him / his |
| مِنْ | مِنْهُ | from him/it |
| فِي | فِيهِ | in him/it |
| إِلَى | إِلَيْهِ | toward him/it |
| عَلَى | عَلَيْهِ | upon him/it |
| إِنَّ | إِنَّهُ | indeed he |
| أَنَّ | أَنَّهُ | that he |
| قَلَم | قَلَمُهُ | his pen |

Signature āyāt: ﴿لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ﴾، ﴿فِيهِ هُدًى وَنُورٌ﴾، ﴿إِنَّهُ هُوَ الْغَفُورُ الرَّحِيمُ﴾.

## سبق 5 — أَنْتَ ("you are", masc.)
**Rule:** أَنْتَ = "تو / تم" (masc.), used to address one male: أَنْتَ يُوسُفُ ("you are
Yusuf"), أَنْتَ رَبٌّ، أَنْتَ نَذِيرٌ، أَنْتَ الْحَقُّ، أَنْتَ مُنْذِرٌ.

## سبق 6 — ـكَ on a noun ("your", masc.)
**Rule:** **ـكَ** on a noun = "تیرا / تیری".
بَيْت → بَيْتُكَ، رَبّ → رَبُّكَ، رَحْمَة → رَحْمَتُكَ، قَوْم → قَوْمُكَ، قَلْب → قَلْبُكَ،
أَهْل → أَهْلُكَ، ابْن → ابْنُكَ، ذِكْر → ذِكْرُكَ، نَفْس → نَفْسُكَ، صَلَاة → صَلَاتُكَ.

## سبق 7 — ـكَ after a particle
Same as lesson 3 but with ـكَ: فِي بَيْتِكَ، مِنْ رَبِّكَ، فِي رَحْمَتِكَ، إِلَى بَيْتِكَ،
مِنْ أَهْلِكَ، مِنْ عِنْدِكَ، مِنْ ذَنْبِكَ، مِنْ جَنَّتِكَ، مِنْ قَوْمِكَ، مِنْ حِسَابِكَ.

## سبق 8 — ـكَ fused onto a particle (and عَنْ)
لَكَ، مِنْكَ، فِيكَ، إِلَيْكَ، عَلَيْكَ، إِنَّكَ، and also **عَنْكَ** (عَنْ + ـكَ).
This lesson introduces the preposition **عَنْ** = "سے / کے بارے میں (about)":
عَنْ قَوْلِكَ، عَنْ سَبِيلِكَ، عَنِ الْآخِرَةِ ("about the Hereafter").
Signature āyāt: ﴿الْحَقُّ مِنْ رَبِّكَ﴾، ﴿إِنَّ رَبَّكَ وَاسِعُ الْمَغْفِرَةِ﴾.

## سبق 9 — هِيَ ("she / it is", fem.)
**Rule:** هِيَ = "وہ" for feminine things (سُورَة، شَجَرَة، كُتُب، أَفْلَا…):
هِيَ فِتْنَةٌ، هِيَ ظَالِمَةٌ، هِيَ بَيْضَاءُ، هِيَ شَاخِصَةٌ، هِيَ خَاوِيَةٌ.

## سبق 10 — ـهَا on a noun ("her / its", fem.)
**Rule:** **ـهَا** on a noun = "اس کا / اس کی" (for a feminine owner/thing).
بَيْت → بَيْتُهَا، رَبّ → رَبُّهَا، زَوْج → زَوْجُهَا، عِلْم → عِلْمُهَا، لَوْن → لَوْنُهَا،
قَلْب → قَلْبُهَا، عَذَاب → عَذَابُهَا، كِتَاب → كِتَابُهَا، أَهْل → أَهْلُهَا، أُمّ → أُمُّهَا.

## سبق 11 — ـهَا after a particle
فِي بَيْتِهَا، مِنْ رَبِّهَا، مِنْ بَعْدِهَا، مِنْ أَهْلِهَا، مِنْ قَوْلِهَا، مِنْ تَحْتِهَا،
مِنْ أَبْوَابِهَا، مِنْ أُخْتِهَا، مِنْ أَطْرَافِهَا.

## سبق 12 — ـهَا fused onto a particle
لَهَا، مِنْهَا، فِيهَا، إِلَيْهَا، عَلَيْهَا، إِنَّهَا، أَنَّهَا. (Same table as lesson 4, with
ـهَا.) Also: عَلَى أَهْلِهَا، بَعْدَ إِصْلَاحِهَا، قَبْلَ غُرُوبِهَا.
Signature: ﴿فِيهَا خَيْرٌ﴾، ﴿لَهَا مَا كَسَبَتْ﴾، ﴿إِنَّهَا تَذْكِرَةٌ﴾.

## سبق 13 — أَنَا ("I am")
**Rule:** أَنَا = "میں" (for male or female speaker): أَنَا يُوسُفُ، أَنَا نَذِيرٌ،
أَنَا بَشَرٌ، أَنَا رَسُولٌ، أَنَا خَيْرٌ، أَنَا نَاصِحٌ.

## سبق 14 — ـي on a noun ("my")
**Rule:** **ـي** on a noun = "میرا / میری".
بَيْت → بَيْتِي، رَبّ → رَبِّي، رَحْمَة → رَحْمَتِي، دِين → دِينِي، صَلَاة → صَلَاتِي،
قَلْب → قَلْبِي، نَفْس → نَفْسِي، رُوح → رُوحِي، ذِكْر → ذِكْرِي، عِبَادَة → عِبَادَتِي،
رَسُول → رَسُولِي. Note the noun's last letter takes a kasra before ـي.

## سبق 15 — ـي after a particle
فِي بَيْتِي، مِنْ رَبِّي، عَلَى نَفْسِي، عَلَى عَيْنِي، عَلَى أُخْرَى، إِلَى بَيْتِي،
مِنْ رَبِّي.

## سبق 16 — ـي fused onto a particle
The 1st-person suffix changes the particle's shape (the consonant often doubles):

| particle | + ـي | meaning |
|----------|------|---------|
| لِـ | لِي | for me |
| مِنْ | مِنِّي | from me |
| فِي | فِيَّ | in me |
| إِلَى | إِلَيَّ | toward me |
| عَلَى | عَلَيَّ | upon me |
| إِنَّ | إِنِّي | indeed I |
| أَنَّ | أَنِّي | that I |

Signature: ﴿إِنِّي رَسُولُ اللهِ﴾، ﴿إِنِّي أَنَا اللهُ﴾، ﴿وَإِنِّي لَغَفَّارٌ﴾.

## سبق 17 — مُجْرِمًا (tanwīn-alif) and the مَفْعُول pattern
**Rule:** a final **ـًا (tanwīn-alif)** on a participle/noun adds the sense "as / being …"
(بحیثیت): مُجْرِم → مُجْرِمًا ("as a criminal"), سَاجِد → سَاجِدًا، خَائِف → خَائِفًا،
يَتِيم → يَتِيمًا، نَبِيّ → نَبِيًّا، مَظْلُوم → مَظْلُومًا، شَيْخ → شَيْخًا. It commonly
attaches after حال words ("being …, in the state of …").

**The مَفْعُول pattern (اسم مفعول):** words on the shape مَفْعُول name the **thing acted
upon** (passive, "done-to"): مَظْلُوم ("one who is wronged"), مَذْكُور ("one who is
mentioned"), مَنْصُور ("one who is helped / given victory"), مَحْفُوظ ("guarded"). These
appear frequently in the Quran and recur in later units.
