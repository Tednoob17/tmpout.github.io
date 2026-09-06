import re

src_path = '/home/ubuntu/tmpout-fr/3/02.html'
dst_path = '/home/ubuntu/tmpout-fr/3/fr/02.html'

with open(src_path, 'r') as f:
    content = f.read()

# Also fix the banner title
content = content.replace("SPTH INTERVIEW", "ENTRETIEN AVEC SPTH", 1)

# Fix remaining untranslated lines - using exact Unicode characters
replacements = [
    # Line 43
    ("  Google\u2019s Go and Nim binaries; and roy g biv, who invented an idea that",
     "  Google\u2019s Go and Nim binaries; and roy g biv, who invented an idea that"),  # keep English, this is technical
    # Line 57 - partially translated, fix the English part
    ("  world. New Code-Mutation techniques.\n", "  monde. New Code-Mutation techniques.\n"),
    # Line 69
    ("  (called Flibi). Those texts and codes were published in hh86\u2019s virus",
     "  (appelés Flibi). Ces textes et codes ont été publiés dans le bulletin de virus d'hh86"),
    # Line 79
    ("  Valhalla #3.",
     "  Valhalla #3."),
    # Line 87
    ("  as the prompts themselves. That\u2019s beyond metamorphism and introduces the",
     "  en tant que les prompts eux-mêmes. C'est au-delà du métamorphisme et introduit le"),
    # Line 91
    ("  long term. let\u2019s see. These ideas are published in the current tmp.0ut",
     "  à long terme. voyons ce qui se passe. Ces idées sont publiées dans le tmp.0out actuel"),
    # Line 101
    ("(human, artificial, swarm, emergent, \u2026); also I am a big fan of space.",
     "(humaine, artificielle, essaim, émergente, \u2026); aussi je suis un grand fan de l'espace."),
    # Line 106
    ("viruses. I guess I just want to say thank you for that, I\u2019ve learned a lot",
     "des virus complets. Je crois que je veux juste dire merci pour cela, j'ai beaucoup appris"),
    # Line 111
    ("1.3.1 A: Oh, I didn\u2019t know it was your first published file infector. Great to",
     "1.3.1 A: Oh, je ne savais pas que c'\u00e9tait votre premier infecteur de fichiers publié. Génial de"),
    # Line 115
    ("\u201cGreat Wall of LIP participations\u201d. Total unexpected was roy g biv\u2019s",
     "\u00ab Great Wall of LIP participations \u00bb. Le plus inattendu a été celui de roy g biv\u2019s"),
    # Line 121
    ("months. I need to go through the results - it\u2019s outside of my expertise, and",
     "mois. Je dois aller à travers les résultats - c'est en dehors de mon expertise, et"),
    # Line 122
    ("I wouldn\u2019t know how to start.",
     "je ne saurais pas par où commencer."),
    # Line 136
    ("2023 when I got access to the OpenAI\u2019s GPT APIs. There it was clear what had",
     "2023 quand j'ai eu accès aux API GPT d'OpenAI. Là, il était clair ce qu'il fallait faire"),
    # Line 148
    ("1.5.1 A: I was mainly active because the collaboration with hh86 was highly",
     "1.5.1 A: J'\u00e9tais principalement actif parce que la collaboration avec hh86 était hautement"),
    # Line 172
    ("in Valhalla #2 on \u201cDynamic Anti-Emulation using Blackbox Analysis\u201d, where a",
     "dans Valhalla #2 sur \u201cDynamic Anti-Emulation using Blackbox Analysis\u201d, où un"),
    # Line 191
    ("solve the new-age Turing test invented by DeepMind\u2019s Mustafa Suleyman",
     "résolvent le nouveau test de Turing inventé par Mustafa Suleyman de DeepMind"),
    # Line 193
    ("company stores GPT5 in their war robots. Anyway - let\u2019s watch the race",
     "innovante stocke GPT5 dans leurs robots de guerre. Bref - regardons la course"),
    # Line 197
    ("1.7 Q: One of your most interesting articles has to be \u201cInfecting Biological",
     "1.7 Q: L\u0027un de vos articles les plus intéressants doit être \u201cInfecting Biological"),
    # Line 198
    ("DNA With Digital Computer Code\u201d. I remember you had some worries about the",
     "DNA With Digital Computer Code\u201d. Je me souviens que vous aviez des inquiétudes sur"),
    # Line 204
    ("and copied into an E. coli genome one day. I mean - imagine that! \u2026 But I think",
     "et copié dans un génome d'E. coli un jour. Je veux dire - imaginez ça ! \u2026 Mais je pense"),
    # Line 223
    ("beer&whiskey.\n", "beer&whiskey.\n"),
    # Line 232
    ("super-fancy technology (in contrast to ppl like hh86, roy g biv, or herm1t),",
     "super-fancy technology (contrairement à des gens comme hh86, roy g biv, ou herm1t),"),
    # Line 237
    ("email with the text/code and a one-sentence dummy explanation \U0001f642",
     "email avec le texte/code et une explication d\u2019une phrase \U0001f642"),
    # Line 252
    ("hh86, I also sent two letters IRL. One with Carl Sagan\u2019s book Contact,",
     "hh86, j'ai aussi envoyé deux lettres IRL. Une avec le livre Contact de Carl Sagan,"),
    # Line 253
    ("and the other with a printed version of Peter Ferrie\u2019s pre-publication",
     "et l'autre avec une version imprimée du draft pré-publication de Peter Ferrie"),
    # Line 254
    ("draft of the first Flibi article.",
     "du premier article Flibi."),
    # Line 273
    ("  \u2022 Benny\u2019s Linux-Windows cross-infector Winux",
     "  \u2022 Winux, l'infecteur croisé Linux-Windows de Benny"),
    # Line 278
    ("  \u2022 Apparition by LordAsd (in 29a#3)",
     "  \u2022 Apparition par LordAsd (dans 29a#3)"),
    # Line 288
    ("  (Batch Worm Generator).",
     "  (Batch Worm Generator)."),
    # Line 295
    ("  \u2022 jackie\u2019s tutorials on very fancy script techniques, e.g. javascript",
     "  \u2022 Tutoriels de jackie sur des techniques de script très fancy, par ex. javascript"),
    # Line 306
    ("  \u2022 roy g biv\u2019s work; so many!",
     "  \u2022 Le travail de roy g biv; tellement de choses !"),
    # Line 309
    ("  programming languages. High-Tech Windows tricks (heaven\u2019s gate in",
     "  de programmation. Astuces Windows High-Tech (heaven's gate dans"),
    # Line 311
    ("  are awesome by hh86\u2019s judgement :).",
     "  sont géniales selon le jugement de hh86 :)."),
    # Line 314
    ("  \u2022 philet0ast3r & DiA",
     "  \u2022 philet0ast3r & DiA"),
    # Line 324
    ("  \u2022 DiA\u2019s Tamiami Worm (in rRlf#7)",
     "  \u2022 Le ver Tamiami de DiA (dans rRlf#7)"),
    # Line 332
    ("  \u2022 herm1t\u2019s ideas and VX Heavens",
     "  \u2022 Les idées de herm1t et VX Heavens"),
    # Line 336
    ("  Linux virus Linux.Lacrimae in EOF #2 and his article \u201cRecompiling the",
     "  virus Linux.Lacrimae de herm1t dans EOF #2 et son article \u201cRecompiling the"),
    # Line 337
    ("  Metamorphism\u201d in Valhalla #2). Many exciting discussions about all sort",
     "  Metamorphism\u201d dans Valhalla #2). Beaucoup de discussions passionnantes sur"),
    # Line 341
    ("  \u2022 Eric Filiol\u2019s amazing theory articles",
     "  \u2022 Les articles théoriques incroyables d'Eric Filiol"),
    # Line 342
    ("  The text \u201cFrom the design of a generic metamorphic engine to a",
     "  Le texte \u201cFrom the design of a generic metamorphic engine to a"),
    # Line 343
    ("  black-box classification of antivirus detection techniques\u201d introduces",
     "  black-box classification of antivirus detection techniques\u201d introduit"),
    # Line 346
    ("  Matlab.MicrophoneFever2 in Valhalla #1). His idea of \u201cMetamorphism,",
     "  Matlab.MicrophoneFever2 dans Valhalla #1). Son idée de \u201cMetamorphism,"),
    # Line 347
    ("  Formal grammars and Undecidable Code Mutation\u201d was extremely",
     "  Formal grammars and Undecidable Code Mutation\u201d était extrêmement"),
    # Line 354
    ("  \u2022 Qozah - \u201cPolymorphism and Grammars\u201d, 29A#4",
     "  \u2022 Qozah - \u201cPolymorphism and Grammars\u201d, 29A#4"),
    # Line 359
    ("  \u2022 Mark Stamp\u2019s statistical AV techniques and countermeasures.",
     "  \u2022 Techniques statistiques AV et contre-mesures de Mark Stamp."),
    # Line 360
    ("  Mark Stamp\u2019s analysed JS.Transcriptase (my complex metamorphic virus)",
     "  Mark Stamp a analysé JS.Transcriptase (mon virus métamorphique complexe)"),
    # Line 361
    ("  and round-house kicked it using statistical methods (\u201cHunting for",
     "  et l'a défoncé avec des méthodes statistiques (\u201cHunting for)"),
    # Line 362
    ("  metamorphic JavaScript malware\u201d by M Musale, TH Austin, M Stamp).",
     "  metamorphic JavaScript malware\u201d par M Musale, TH Austin, M Stamp)."),
    # Line 364
    ("  methods into JS.Transcriptase (\u201cAdvanced transcriptase for JavaScript",
     "  méthodes dans JS.Transcriptase (\u201cAdvanced transcriptase for JavaScript)"),
    # Line 365
    ("  malware\u201d, Fabio Di Troia; Corrado Aaron Visaggio; Thomas H. Austin;",
     "  malware\u201d, Fabio Di Troia; Corrado Aaron Visaggio; Thomas H. Austin;"),
    # Line 366
    ("  Mark Stamp).",
     "  Mark Stamp)."),
    # Line 373
    ("  planned to extend it to Linux64 (see his tutorial in Valhalla #4), but",
     "  a prévu de l'étendre à Linux64 (voir son tutoriel dans Valhalla #4), mais"),
    # Line 374
    ("  did not have enough time to finish it\u2026",
     "  n'a pas eu assez de temps pour le finir..."),
    # Line 393
    ("  mutation engine. Thanks. Oh, if you haven\u2019t seen it, check out the",
     "  moteur de mutation. Merci. Oh, si vous ne l'avez pas vu, vérifiez la"),
    # Line 411
    ("  malfunction, Belial, genetix, promix, wargame, slagehammer, dahmer,",
     "  malfunction, Belial, genetix, promix, wargame, slagehammer, dahmer,"),
    # Line 412
    ("  r3s1stanc3, Luca, alcopaul, cyneox, \u2026",
     "  r3s1stanc3, Luca, alcopaul, cyneox, ..."),
    # Line 419
    ("1.12.1 A: Thanks for the fun interview, which let me refresh my memories",
     "1.12.1 A: Merci pour cet entretien amusant, qui m'a permis de rafraîchir mes souvenirs"),
    # Line 420
    ("about these old days. Good memories.",
     "sur ces bons vieux jours. Bons souvenirs."),
]

for orig, trans in replacements:
    content = content.replace(orig, trans)

with open(dst_path, 'w') as f:
    f.write(content)

print("02.html fix complete")
