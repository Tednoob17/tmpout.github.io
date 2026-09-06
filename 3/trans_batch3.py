import re

def translate_file(src_path, dst_path, title_fr, translations):
    with open(src_path, 'r') as f:
        content = f.read()
    
    content = re.sub(r'<title>.*?</title>', f'<title>{title_fr}</title>', content)
    
    for orig, trans in translations:
        content = content.replace(orig, trans)
    
    credit = '\n[ Traduction par Tedsig42 ]\n'
    if '</pre></div></body>' in content:
        content = content.replace('</pre></div></body>', credit + '</pre></div></body>')
    elif '</pre></div>' in content:
        content = content.replace('</pre></div>', credit + '</pre></div>')
    
    with open(dst_path, 'w') as f:
        f.write(content)
    
    print(f"Translated: {dst_path}")

# 04.html - Hijacking __cxa_finalize
translate_file('/home/ubuntu/tmpout-fr/3/04.html', '/home/ubuntu/tmpout-fr/3/fr/04.html',
    "Hijacking de __cxa_finalize pour obscurcir le point d'entrée", [
    ("Hijacking __cxa_finalize to achieve entry point obscuring", "Hijacking de __cxa_finalize pour obscurcir le point d'entrée"),
    ("~ vrzh", "~ vrzh"),
    ("Hijacking the destruction mechanism is an effective entry point obscuring (EPO)", 
     "Hijacker le mécanisme de destruction est une technique efficace d'obscurcissement du point d'entrée (EPO)"),
    ("virus technique, so long as the delayed execution doesn't impede functionality", "technique de virus, tant que l'exécution différée n'empêche pas le fonctionnement"),
    ("of the virus or the host. A common example of this technique is patching the", "du virus ou de l'hôte. Un exemple commun de cette technique est de patcher"),
    ("the destructor array. In the first tmp.out issue [0], s01den and sblip", "le tableau des destructeurs. Dans le premier numéro de tmp.out [0], s01den et sblip"),
    ("published their Linux.Eng3ls virus, which used this EPO technique. The virus", "ont publié leur virus Linux.Eng3ls, qui utilisait cette technique EPO. Le virus"),
    ("also uses a number of other cool techniques and I strongly recommend you check", "utilise également un certain nombre d'autres techniques sympas et je vous recommande vivement"),
    ("it out, as well as s01den's follow-up note on EPO techniques in tmp.out #2 [1].", "d'aller voir, ainsi que la note complémentaire de s01den sur les techniques EPO dans tmp.out #2 [1]."),
    ("The C++ ABI spec exposes another, less obvious target for hijacking code", "La spécification de l'ABI C++ expose une autre cible, moins évidente, pour le piratage de code"),
    ("execution - __cxa_finalize(). In this txt I'm going to describe the purpose of", "d'exécution - __cxa_finalize(). Dans cet article je vais décrire le but de"),
    ("__cxa_finalize(), touch on how it fits in the ELF destruction process, and", "__cxa_finalize(), expliquer comment il s'inscrit dans le processus de destruction ELF,"),
    ("present two methods of hijacking it.", "et présenter deux méthodes pour le pirater."),
    ("Two pieces of my code supplement this txt:", "Deux morceaux de mon code accompagnent cet article :"),
    ("  ▪ A virus Linux.ElizaCanFix, which implements Method 0.", "  ▪ Un virus Linux.ElizaCanFix, qui implémente la Méthode 0."),
    ("  ▪ An infector [2] written in C, which implements both hijacking methods.", "  ▪ Un infecteur [2] écrit en C, qui implémente les deux méthodes de piratage."),
    ("Both programs use Silvio Cesare's text segment padding infection [3], but any", "Les deux programmes utilisent l'infection par remplissage de segment de texte de Silvio Cesare [3],"),
    ("other infection method can be used. Detailing the infection method is out of", "mais toute autre méthode d'infection peut être utilisée. Le détail de la méthode d'infection"),
    ("the scope of this txt.", "sort du cadre de cet article."),
])

# 23.html - silent syscall hooking on arm64 linux
translate_file('/home/ubuntu/tmpout-fr/3/23.html', '/home/ubuntu/tmpout-fr/3/fr/23.html',
    "hookage silencieux d'appels système sur arm64 linux via le gestionnaire svc", [
    ("----> silent syscall hooking on arm64 linux via patching svc handler <----",
     "----> hookage silencieux d'appels système sur arm64 linux via le gestionnaire svc <----"),
    ("#### [introduction] ####", "#### [introduction] ####"),
    ("system call hooking on linux is quite trivial. current common techniques include:",
     "le hookage d'appels système sous linux est assez trivial. les techniques courantes incluent :"),
    ("- using the kernel ftrace api", "- utiliser l'API ftrace du noyau"),
    ("- modifying sys_call_table to point to your own table", "- modifier sys_call_table pour pointer vers votre propre table"),
    ("- modifying addresses in sys_call_table to point to your own code", "- modifier les adresses dans sys_call_table pour pointer vers votre propre code"),
    ("- patching the syscall entries themselves", "- patcher les entrées des appels système elles-mêmes"),
    ("unfortunately, even userland rootkit scanners can detect the first 2 methods-",
     "malheureusement, même les scanners de rootkits en mode utilisateur peuvent détecter les 2 premières méthodes -"),
    ("via periodically checking /proc/kallsyms or system.map.", "en vérifiant périodiquement /proc/kallsyms ou system.map."),
    ("current kernel mode rootkit scanners will easily detect all of these methods.",
     "les scanners de rootkits en mode noyau détecteront facilement toutes ces méthodes."),
    ("rain king patches el0_svc_common, which is invoked by the exception handler on a svc",
     "rain king patche el0_svc_common, qui est invoqué par le gestionnaire d'exceptions sur un svc"),
    ("el0_svc_common then redirects execution to the syscall entry via looking up its address in",
     "el0_svc_common redirige ensuite l'exécution vers l'entrée de l'appel système en cherchant son adresse dans"),
    ("sys_call_table.", "sys_call_table."),
    ("rain king then checks the # of the syscall and redirects execution to two different tables -",
     "rain king vérifie ensuite le numéro de l'appel système et redirige l'exécution vers deux tables différentes -"),
    ("depending on if the syscall # is marked as hooked.", "en fonction de savoir si le numéro d'appel système est marqué comme hooké."),
    ("this leaves the sys_call_table and the entries it points to unmodified.",
     "cela laisse sys_call_table et ses entrées inchangées."),
    ("as far as i am aware, no current rootkit scanner currently detects this,",
     "pour autant que je sache, aucun scanner de rootkit actuel ne détecte cela,"),
    ("although doing so could be as trivial as periodically comparing a checksum of kernel code to a base",
     "bien qu'il pourrait être aussi simple que de comparer périodiquement une somme de contrôle du code noyau à une valeur de base"),
    ("value, perhaps with a trustzone driver.", "peut-être avec un pilote trustzone."),
    ("#### [hooking el0_svc_common] ####", "#### [hookage de el0_svc_common] ####"),
    ("{0.} ---- overview ----", "{0.} ---- aperçu ----"),
    ("since el0_svc_common is blacklisted from ftrace, we will be manually splicing our hook !",
     "comme el0_svc_common est dans la liste noire de ftrace, nous allons manuellement splisser notre hook !"),
    ("splicing a function entails:", "spliser une fonction implique :"),
    ("- compiling our \"hook\" (the function to be redirected to when the hook-ee executes)-",
     "- compiler notre \"hook\" (la fonction à rediriger quand le hooké s'exécute)-"),
    ("  with &lt;trampoline size&gt; nops", "  avec &lt;taille du trampoline&gt; nops"),
    ("- copying the first, &lt;trampoline size&gt; instructions of hook-ee to our hook",
     "- copier les premières instructions, &lt;taille du trampoline&gt;, du hooké vers notre hook"),
    ("- copying our trampoline to the hooked function", "- copier notre trampoline vers la fonction hookée"),
    ("when the hook-ee is called, our trampoline will jump to our hook,",
     "quand le hooké est appelé, notre trampoline saute vers notre hook,"),
    ("the hook can now modify the arguments of the hook-ee.", "le hook peut maintenant modifier les arguments du hooké."),
    ("once the hook is finished, it will jump to the hooked function entry + &lt;trampoline size&gt;.",
     "une fois le hook terminé, il saute vers l'entrée de la fonction hookée + &lt;taille du trampoline&gt;."),
    ("{0.1.} layout of things post hook installation", "{0.1.} disposition des éléments après l'installation du hook"),
    ("{1.} ---- copying sys_call_table ----", "{1.} ---- copie de sys_call_table ----"),
    ("we will begin by calling vmalloc (since sys_call_table can span multiple pages and must be page aligned)",
     "nous commençons par appeler vmalloc (puisque sys_call_table peut s'étendre sur plusieurs pages et doit être aligné sur une page)"),
    ("on a new table, and copying the original table into it. this will be our \"malicious\" table that",
     "sur une nouvelle table, et copions la table originale dedans. Ceci sera notre table \"malicieuse\" qui"),
    ("we will re-direct hooked syscalls to.", "nous redirigerons les appels système hookés vers elle."),
    ("{2.} ---- disabling write-protect via pagetable ----", "{2.} ---- désactivation de la protection en écriture via la table de pages ----"),
    ("since we need to write to both el0_svc_common, and el0_svc_common_hook, and both exist in",
     "puisque nous devons écrire sur el0_svc_common et el0_svc_common_hook, et les deux existent en"),
    ("write-protected memory. we will get the page table entry for both functions and then set the write",
     "mémoire protégée en écriture. Nous obtenons l'entrée de la table de pages pour les deux fonctions et définissons ensuite le bit d'écriture"),
    ("bit in the entry like so:", "dans l'entrée comme suit :"),
    ("{3.} ---- stop_machine ----", "{3.} ---- stop_machine ----"),
    ("to repeat the wise words of a friend,", "Pour répéter les paroles sagues d'un ami,"),
    ('it would cause "horrific crashes" if an interrupt were to... interrupt our copying and execute',
     'il causerait des "plantAGES horribles" si une interruption interrompait notre copie et exécutait'),
    ("el0_svc_common, or if we were to copy our trampoline while a CPU is mid-execution in el0_svc_common.",
     "el0_svc_common, ou si nous copions notre trampoline pendant qu'un CPU est en cours d'exécution dans el0_svc_common."),
    ("to prevent this, we will use stop_machine. ill let the documentation speak for itself:",
     "Pour prévenir cela, nous utiliserons stop_machine. Laissez la documentation parler pour elle-même :"),
    ("in hook.c we call copy_shellcode_sync, the function that copies the trampoline with stop_machine",
     "dans hook.c nous appelons copy_shellcode_sync, la fonction qui copie le trampoline avec stop_machine"),
    ("pretty overkill, huh.", "plutôt overkill, non ?"),
    ("{3.} ---- JIT assembling shellcode ----", "{3.} ---- assemblage JIT du shellcode ----"),
    ("as i was writing the trampoline shellcode, i ran into an issue.",
     "en écrivant le shellcode du trampoline, je suis tombé sur un problème."),
    ("in order to jump our hook, we need to load its address,",
     "pour sauter vers notre hook, nous devons charger son adresse,"),
    ("due to KASLR, we have no idea what the address of our hook is at compile time.",
     "en raison de KASLR, nous n'avons aucune idée de l'adresse de notre hook au moment de la compilation."),
    ("well the only solution to this is to assemble the trampoline shellcode AT RUNTIME !",
     "Eh bien, la seule solution consiste à assembler le shellcode du trampoline À LA VOLÉE !"),
    ("this is actually easier than it sounds.", "C'est en fait plus facile qu'il n'y paraît."),
    ("since instructions are 32 bits, loading a 64 bit address as an immediate is out of the question so",
     "puisque les instructions sont sur 32 bits, charger une adresse 64 bits comme valeur immédiate est hors de question, donc"),
    ("we have two options:", "nous avons deux options :"),
    ("i choose the latter option out of laziness, since i only need to write an assembler for on instruction, movk.",
     "je choisis la dernière option par paresse, car je n'ai besoin d'écrire un assembleur que pour une instruction, movk."),
    ("the assembler itself is very simple, we simply shift all parameters to their correct positions,",
     "l'assembleur lui-même est très simple, nous décalons simplement tous les paramètres à leurs positions correctes,"),
    ("then OR them with each other.", "puis les OU ensemble."),
    ("the assembler itself is very simple, we simply shift all parameters to their correct positions,",
     "l'assembleur lui-même est très simple, nous décalons simplement tous les paramètres à leurs positions correctes,"),
    ("then OR them with each other.", "puis les OU ensemble."),
    ("to assemble an absolute load of a 64 bit address, we use bitmasks to break the address into 16 bit chunks,",
     "pour assembler un chargement absolu d'une adresse 64 bits, nous utilisons des masques binaires pour diviser l'adresse en fragments de 16 bits,"),
    ("and then assemble movk with incremented shifts.", "puis assembler movk avec des décalages incrémentés."),
    ("opc: opcode of movk", "opc : opcode de movk"),
    ("imm16: 16 bit immediate to load", "imm16 : valeur immédiate 16 bits à charger"),
    ("hw: shift / 16", "hw : décalage / 16"),
    ("rd: destination register", "rd : registre de destination"),
    ("the assembler itself is very simple, we simply shift all parameters to their correct positions,", "L'assembleur lui-même est très simple, nous décalons simplement tous les paramètres à leurs positions correctes,"),
    ("then OR them with each other.", "puis les OU ensemble."),
    ("to assemble an absolute load of a 64 bit address, we use bitmasks to break the address into 16 bit chunks,", "Pour assembler un chargement absolu d'une adresse 64 bits, nous utilisons des masques binaires pour diviser l'adresse en fragments de 16 bits,"),
    ("and then assemble movk with incremented shifts.", "puis assembler movk avec des décalages incrémentés."),
    ("{4.} ---- copying shellcode ----", "{4.} ---- copie du shellcode ----"),
    ("now we are free to copy away !", "maintenant nous sommes libres de copier !"),
    ("first saving the first few instructions of el0_svc_common to", "nous sauvegardons d'abord les premières instructions d'el0_svc_common vers"),
    ("el0_svc_common_hook then copying our shellcode (trampoline) to el0_svc_common.", "el0_svc_common_hook, puis nous copions notre shellcode (trampoline) vers el0_svc_common."),
    ("#### [el0_svc_common_hook] ####", "#### [el0_svc_common_hook] ####"),
    ("{0.} ---- disassembly of el0_svc_common + source ----", "{0.} ---- désassemblage de el0_svc_common + source ----"),
    ("okay, now that we have successfully hooked el0_svc_common, how are we going to redirect the table ?",
     "d'accord, maintenant que nous avons réussi à hooker el0_svc_common, comment allons-nous rediriger la table ?"),
])

# 24.html - HVice
translate_file('/home/ubuntu/tmpout-fr/3/24.html', '/home/ubuntu/tmpout-fr/3/fr/24.html',
    'HVice - électronique de contre-mesure anti-intrusion hyperviseur', [
    ("Intrusion Countermeasure Electronics v0.4", "Intrusion Countermeasure Electronics v0.4"),
    ("hvICE is a proof of concept implementation of hypervisor enforced code/data integrity for the Linux",
     "hvICE est'une implémentation proof-of-concept d'EPI (intégrité du code/données) imposée par l'hyperviseur pour le"),
    ("kernel using xen and libvmi. It requires no modification to the guest OS. hvICE achieves this by", "noyau Linux utilisant xen et libvmi. Il ne nécessite aucune modification du système invité. hvICE"),
    ("setting all pages between _text and _etext and all of kernel rodata to not writable in the guests", "y parvient en définissant toutes les pages entre _text et _etext et toute la rodata du noyau comme"),
    ("EPT, then pausing the VM and logging the violation if an attempted write did not come from within", "non accessibles en écriture dans l'EPT de l'invité, puis en mettant en pause la VM et en consignant la"),
    ("kernel text. Writes by code within kernel text are ignored to prevent false positives due to kernel", "violation si une écriture non provenant du texte noyau n'a pas eu lieu. Les écritures par du code"),
    ("self patching.", "à l'intérieur du texte noyau sont ignorées pour éviter les faux positifs dus au"),
    ("self patching.", "auto-patch du noyau."),
    ("Example:", "Exemple :"),
    ("- Kernel self protection is insufficiently secure.", "- La protection du noyau n'est pas suffisamment sécurisée."),
    ("- Despite recent kernel versions preventing writes to cr0 and setting protected pages as writeable",
     "- Malgré les versions récentes du noyau qui empêchent l'écriture dans cr0 et définissent les pages"),
])

print("Done translating 04, 23, 24")
PYEOF