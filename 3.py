import requests
from bs4 import BeautifulSoup
list=[
 "Epitomized", "Hidebound", "Languish", "Obsequious", "Polemical", "Restorative", "Thwart", "Adamant", "Brawny", "Decathlon", "Equivocate", "Hieroglyphics", "Larceny", "Obsession", "Ponderous", "Retention", "Timorous", "Adroit", "Brevity", "Decorum", "Err", "Hinder", "Largess", "Obsolete", "Pontificate", "Reticent", "Tirade", "Adulation", "Bristle", "Decoy", "Erratic", "Histrionic", "Laud", "Obstreperous", "Portend", "Retraction", "Titter", "Adversity", "Broach", "Deference", "Esoteric", "Hoary", "Lavish", "Obtuse", "Portent", "Revere", "Tome", "Advocate", "Brusque", "Defoliate", "Espouse", "Hone", "Lax", "Obviate", "Poseur", "Riddled", "Torpid", "Aesthetic", "Bulwark", "Defunct", "Etymology", "Hyperbole", "Legend", "Odious", "Posterity", "Rife", "Torpor", "Affable", "Bureaucracy", "Degradation", "Eulogy", "Hypochondriac", "Legion", "Officious", "Posthumous", "Rigor", "Totter", "Alacrity", "Burgeon", "Deleterious", "Euphemism", "Hypocritical", "Lethargic", "Ogle", "Postulate", "Robust", "Tractable", "Alchemy", "Burnish", "Deliberate", "Euphony", "Iconoclast", "Levity", "Olfactory", "Potable", "Rotund", "Tranquil", "Alibi", "Buttress", "Delineation", "Evacuate", "Idiosyncrasy", "Libertarian", "Ominous", "Potent", "Ruminate", "Transcribe", "Allay", "Byline", "Demur", "Exacerbate", "Ignominious", "Liniment", "Omnipotent", "Pragmatic", "Ruse", "Transgress", "Alleviate", "Cacophony", "Denounce", "Exasperated", "Ignominy", "Lithe", "Omniscient", "Pragmatist", "Saccharin", "Transient", "Aloof", "Cajole", "Deplete", "Exceptionable", "Illuminate", "Livid", "Onerous", "Preamble", "Sacrosanct", "Traverse", "Altruism", "Caldron", "Deplore", "Exculpate", "Illusory", "Lobbyist", "Onus", "Precarious", "Sagacious", "Trepidation", "Amass", "Callow", "Depravity", "Execrable", "Immoderate", "Lofty", "Opaque", "Precedent", "Sage", "Trinket", "Ambiguity", "Candid", "Deprecate", "Exegesis", "Immutable", "Longevity", "Opulent", "Precept", "Salacious", "Trite", "Ambiguous", "Candor", "Deride", "Exemplary", "Impartial", "Loquacious", "Ordain", "Precinct", "Sallow", "Trivial", "Ambivalence", "Cantankerous", "Derogatory", "Exemplify", "Impecunious", "Lucid", "Ornate", "Precipice", "Salubrious", "Truant", "Ambulatory", "Capacious", "Desecrate", "Exhaustive", "Impious", "Ludicrous", "Orthodox", "Precipitous", "Salutary", "Truncate", "Ameliorate", "Capitulate", "Desecration", "Exonerates", "Impoverished", "Lukewarm", "Ossify", "Preclude", "Sanctimonious", "Tumult", "Amelioration", "Carping", "Desist", "Exorcism", "Impromptu", "Lummox", "Ostentatious", "Precocious", "Sanction", "Turpitude", "Amiable", "Cartographer", "Despondent", "Expatriate", "Inadvertent", "Luscious", "Oust", "Predecessor", "Sanguinary", "Tyro", "Amity", "Castigate", "Destitution", "Expedient", "Incantation", "Lynch", "Overt", "Predicament", "Sanguine", "Ubiquitous", "Amorphous", "Catharsis", "Deter", "Expedite", "Incarceration", "Machinations", "Overwrought", "Preeminent", "Sardonic", "Unalloyed", "Analgesic", "Caucus", "Deteriorate", "Exposition", "Incessant", "Maelstrom", "Palatable", "Prerogative", "Savant", "Unctuous", "Analogous", "Caustic", "Detrimental", "Extol", "Incipient", "Magnanimous", "Palisade", "Prescient", "Scale", "Undermined", "Anarchy", "Cavalcade", "Devoured", "Extradite", "Inclination", "Magnate", "Palliative", "Presentiment", "Scapegoat", "Underscore", "Anecdote", "Celerity", "Dexterous", "Extraneous", "Incoherent", "Maladroit", "Pallid", "Presumptuous", "Scrupulous", "Unequivocal", "Animosity", "Censorious", "Dichotomy", "Extrapolate", "Incongruous", "Malady", "Palpable", "Pretentious", "Scrutinize", "Unfetter", "Annex (n)", "Censure", "Didactic", "Extrinsic", "Inconsequential", "Malediction", "Panacea", "Prevaricate", "Scuttle", "Unfrock", "Annex (v)", "Cerebral", "Diffident", "Fallacious", "Inconspicuous", "Malefactor", "Paradigm", "Pristine", "Seminary", "Unprecedented", "Anomaly", "Certitude", "Digress", "Falter", "Indelible", "Malinger", "Paradox", "Proclivity", "Sensuous", "Unscathed", "Antagonism", "Charlatan", "Dike", "Fanatical", "Indifferent", "Malingerer", "Paragon", "Procrastinate", "Sentinel", "Unwitting", "Antagonistic", "Chary", "Dilatory", "Fanaticism", "Indigenous", "Malleable", "Paramount", "Prodigal", "Sequester", "Upbraid", "Antediluvian", "Chastises", "Dilemma", "Fastidious", "Indolence", "Mallet", "Parasite", "Prodigious", "Serendipity", "Uproarious", "Anthology", "Chicanery", "Dilettante", "Fatuous", "Inductee", "Manipulatable", "Parched", "Profane", "Serene", "Upshot", "Anthropocentrism", "Chimerical", "Diligent", "Feasible", "Indulgent", "Marred", "Pariah", "Profanity", "Serrated", "Urbane", "Antiquated", "Choleric", "Diorama", "Fecund", "Inebriation", "Marshal", "Parity", "Profound", "Servile", "Usurp", "Apathetic", "Chronicler", "Dirge", "Felicitous", "Ineffable", "Marsupial", "Parochial", "Profundity", "Skeptical", "Utilitarian", "Apathy", "Circuitous", "Disapprobation", "Fervor", "Inept", "Martinet", "Parody", "Proletarian", "Skirmish", "Utopian", "Apocryphal", "Circumlocution", "Discern", "Fickle", "Inertia", "Masochist", "Parry", "Prolific", "Sluggard", "Vacillate", "Appease", "Circumscribe", "Discord", "Finesse", "Inevitable", "Matriarchy", "Parsimonious", "Proponents", "Smelt", "Vacuous", "Apprehensive", "Circumspect", "Discordancy", "Fitful", "Inexorable", "Maverick", "Parsimony", "Prosaic", "Smorgasbord", "Vagrant", "Arable", "Circumvent", "Discrepancy", "Flagrant", "Inexpedient", "Meager", "Partisan", "Proscribe", "Solace", "Vapid", "Arbitrary", "Clairvoyant", "Discriminate", "Flamboyant", "Infallible", "Meander", "Pathos", "Prosody", "Solicit", "Variegated", "Arcane", "Clamor", "Discursiveness", "Flaunt", "Infamous", "Mellow", "Patron", "Prostration", "Somnambulist", "Vehemence", "Archaic", "Clandestine", "Disdain", "Flippant", "Infer", "Menagerie", "Patronize", "Protagonist", "Soothsayer", "Vehement", "Archetype", "Clemency", "Disinterested", "Flout", "Ing�nue", "Mendacious", "Paucity", "Protean", "Sophomoric", "Venal", "Archives", "Clich�", "Disparage", "Flustered", "Ingrate", "Mercenary", "Peccadillo", "Prot�g�", "Soporific", "Veneer", "Articulate", "Clientele", "Disparity", "Fly-by-night", "Inimical", "Mercurial", "Pedant", "Protocol", "Sparse", "Venerate", "Artifice", "Coalesce", "Dispassionate", "Forensic", "Innate", "Merge", "Pedestrian", "Provincial", "Specious", "Venial", "Artisan", "Coddle", "Disseminating", "Fortitude", "Innocuous", "Metaphorically", "Peerless", "Prudent", "Speckled", "Veracity", "Ascetic", "Coercion", "Diurnal", "Fortuitous", "Innovate", "Meticulous", "Pejorative", "Puerile", "Sporadic", "Verbose", "Assiduous", "Cogent", "Divert", "Fractious", "Inscrutable", "Mettle", "Pellucid", "Punctilious", "Spurious", "Verbosity", "Assuage", "Cogitate", "Docile", "Fraudulent", "Insentient", "Milieu", "Pensive", "Purloin", "Stagnant", "Vertigo", "Astute", "Collage", "Dogmatic", "Frivolous", "Insipid", "Mire", "Penury", "Pusillanimous", "Staid", "Vestigial", "Asylum", "Collate", "Dolt", "Frugal", "Instigate", "Misanthrope", "Perceptive", "Pyromania", "Stanza", "Vignette", "Atheist", "Colloquial", "Dotard", "Furrow", "Instigator", "Misnomer", "Percipient", "Quaff", "Staunch", "Vilification", "Atrophy", "Collusion", "Drawl", "Furtive", "Insurgent", "Misogynist", "Perdition", "Quagmire", "Stereotype", "Vindicate", "Attenuate", "Commandeer", "Drivel", "Futile", "Interminable", "Misrepresentation", "Peremptory", "Quaint", "Stevedore", "Virtuoso", "Augment", "Complacent", "Droll", "Galleon", "Intermittent", "Mitigate", "Perfidy", "Quandary", "Stifle", "Virulent", "Auspicious", "Compliant", "Drone", "Gambol", "Intransigence", "Modicum", "Perfunctory", "Quarantine", "Stoic", "Vital", "Austere", "Concatenate", "Dubious", "Garble", "Intransigent", "Momentous", "Peripatetic", "Quarry", "Stoke", "Vitriolic", "Aversion", "Concatenation", "Dupe", "Garish", "Intrepid", "Monotonous", "Peripheral", "Querulous", "Stolid", "Vivacity", "Balk", "Conciliate", "Dynamic", "Garner", "Inveterate", "Moratorium", "Perjury", "Quirk", "Stratagem", "Vivify", "Banal", "Concise", "Ebullient", "Garrulous", "Invidious", "Moribund", "Pernicious", "Ramble", "Strident", "Vociferous", "Banality", "Condescend", "Eccentric", "Gaunt", "Inviolable", "Morose", "Persnickety", "Ramifications", "Stringent", "Volatile", "Bane", "Condone", "Eclectic", "Genre", "Irascible", "Mundane", "Perpetuated", "Rancor", "Strut", "Voluble", "Bard", "Condoning", "Edifice", "Germane", "Ire", "Munificent", "Perpetuity", "Rant", "Stupefying", "Voluminous", "Bastion", "Conflagration", "Efface", "Germinal", "Irksome", "Mutinous", "Personable", "Ratify", "Subpoena", "Voracious", "Befuddle", "Confound", "Effigy", "Gibbering", "Ironic", "Myriad", "Perspicacious", "Raucous", "Substantiate", "Waive", "Begrudge", "Congeal", "Effusive", "Glacial", "Irrational", "Navigable", "Perspicacity", "Raze", "Subterfuge", "Wane", "Beguile", "Congenital", "Egalitarianism", "Goad", "Irreproachable", "Nebulous", "Pertinent", "Rebuttal", "Subtle", "Wary", "Belabor", "Connoisseur", "Egregious", "Grate (v)", "Irrevocable", "Nefarious", "Peruse", "Recant", "Subversive", "Wax", "Beleaguer", "Consecrate", "Egress", "Gratis", "Itinerant", "Negate", "Pervasive", "Recapitulate", "Succinct", "Waylay", "Belie", "Consensus", "Eloquent", "Gratuitous", "Jaded", "Negligence", "Petrify", "Receptacle", "Suffragist", "Weighty", "Belittle", "Conspicuous", "Elucidate", "Gravity", "Jargon", "Neologism", "Petulant", "Recluse", "Supercilious", "Whelp",

"Bellicose", "Consummate", "Elusive", "Gregarious", "Jaundiced", "Nettle", "Phenomenon", "Recuperate", "Superlative", "Whet", "Belligerent", "Contemporary", "Emaciated", "Gritty", "Jaunt", "Niggardly", "Philanthropy", "Red tape", "Surly", "Whimsical", "Bemoan", "Contrite", "Emancipate", "Guffaw", "Jeopardize", "Nomadic", "Philistine", "Redolent", "Surreptitious", "Willful", "Benevolent", "Contrition", "Embezzle", "Guile", "Jingoistic", "Nonchalance", "Phlegmatic", "Redress", "Surreptitiously", "Wily", "Benign", "Contumacious", "Embroil", "Guileless", "Jocular", "Nondescript", "Pillage", "Redundant", "Susceptible", "Wispy", "Benignity", "Contusion", "Emerge", "Gullibility", "Jollity", "Nonentity", "Pinnacle", "Referendum", "Suspect", "Wistful", "Bequeath", "Conundrum", "Emulate", "Gullible", "Jubilant", "Nostalgia", "Pious", "Refute", "Sybarite", "Zany", "Berate", "Conventional", "Endorse", "Gustatory", "Judicious", "Notoriety", "Pivotal", "Regale", "Sycophant", "Zeal", "Beret", "Corpulent", "Endurance", "Hackneyed", "Jurisprudence", "Novel", "Placate", "Relegate", "Taciturn", "Zealot", "Bestial", "Corrugated", "Enduring", "Hallowed", "Juxtapose", "Novice", "Placebo", "Remorse", "Tactile", "Zenith", "Abate", "Abjure", "Blandishment", "Boor", "Cardinal", "Deliberate", "Equivocation", "Feckless", "Imperturbability", "Meretricious", "Augury", "Boycott", "Glib", "Incise", "Moralistic", "Ostracism", "Penchant", "Rarefy", "Repine", "Stipulate", "Diaphanous", "Feint", "Inured", "Mettlesome", "Puissance", "Recondite", "Stygian", "Touting", "Virtuosity", "Volubility", "Caret", "Contiguous", "Damp", "Ellipsis", "Extirpation", "Foppish", "Gaffe", "Hortatory", "Opprobrious", "Recumbent", "Ambidextrous", "Culpability", "Discernment", "Encomium", "Inveigle", "Minatory", "Ossified", "Plumb", "Quintessential", "Runic", "Accretion", "Anachronistic", "Chronic", "Churlishness", "Demagogue", "Effrontery", "Idyll", "Interregnum", "Nugatory", "Sinecure", "Anodized", "Aphoristic", "Canonical", "Commensurate", "Dexterity", "Extant", "Impugned", "Probity", "Raconteur", "Solicitous", "Amalgamate", "Baleful", "Coerce", "Inchoate", "Iniquitous", "Libertine", "Millinery", "Natty", "Occluded", "Sidereal", "Avaricious", "Extirpate", "Halcyon", "List (v)", "Maudlin", "Refulgent", "Subliminal", "Testiness", "Vituperate", "Whittle", "Colander", "Cumbersome", "Diaphanous", "Dispatch", "Epistemology", "Froward", "Supine", "Throwback", "Untoward", "Verisimilar", "Abysmal", "Approbation", "Bent (n)", "Cadge", "Debacle", "Extemporize", "Incumbents", "Lambaste", "Noisome", "Pastiche", "Arboreal", "Centrifuge", "Cloistered", "Disabuse", "Engendering", "Intemperate", "Lugubrious", "Nonplussed", "Pedagogy", "Satiate", "Slake", "Artless", "Comeliness", "Doff", "Don", "Erudition", "Plaintive", "Suborn", "Tendentious", "Tortuous", "Verbiage", "Atonement", "Complaisance", "Daguerreotype", "Fawn", "Gregariousness", "Nascent", "Paean", "Reproof", "Scurvy", "Tutelary", "Abscission", "Contentious", "Debilitating", "Foible", "Importune", "Pertain", "Slew", "Toady", "Torrid", "Veracious", "Asperity", "Blowhard", "Disingenuous", "Evanescent", "Intangible", "Labile", "Malapropism", "Posture (v)", "Proximate", "Pugnacious", "Foreshadowed", "Gaucherie", "Heterodox", "Inscrutability", "Limerick", "Mannered", "Pluck (n)", "Sedulous", "Syllogism", "Vicissitude", "Acolyte", "Admonitory", "Caprices", "Cornucopia", "Deferential", "Intractability", "Luminary", "Minion", "Undergird", "Vitiate", "Coterie", "Denigrate", "Empirical", "Gainsay", "Hyperbole", "Modest", "Prolixity", "Rebus", "Sere", "Vulpine", "Corroborate", "Exacerbated", "Exact (v)", "Faddish", "Hapless", "Misconstrue", "Perennial", "Rent", "Shard", "Xenophobe", "Alleviated", "Apostrophe", "Centurion", "Emollient", "Fusillade", "Inerrancy", "Mince", "Palpate", "Platitude", "Quibble", "Apprehension", "Conniving", "Derision", "Epigram", "Lassitude", "Pedantic", "Phenomenology", "Precipitate", "Renege", "Armada", "Dawdler", "Dross", "Expiate", "Hack", "Prone", "Propensity", "Scabbard", "Skiff", "Umbrage", "Dilettantism", "Enervate", "Malevolent", "Neophyte", "Panegyric", "Presage", "Serration", "Slight", "Tare", "Unprepossessing", "Aberration", "Cant", "Disinter", "Fa�ade", "Impeding", "Lacuna", "Monolithic", "Pied", "Roster", "Seemly", "Analogue", "Coda", "Commingle", "Equivocal", "Fallible", "Hallow", "Indigence", "Papyrus", "Pique", "Sap", "Arbitrator", "Descry", "Facetious", "Indecorous", "Proliferate", "Scotch (v)", "Strut", "Toy (v)", "Usury", "Wag (n)", "Atavism", "Filibuster", "Gambit", "Mitigation", "Obligate", "Predilection", "Propitiate", "Stanch", "Travesty", "Waft", "Forage", "Lumber", "Muse", "Prescience", "Prune", "Ready", "Resolve", "Squalid", "Sullied", "Veneration", "Demur", "Duplicity", "Exigency", "Expostulate", "Gossamer", "Inefficacious", "Pine", "Prudish", "Quixotic", "Stipple", "Abrasion", "Adumbrate", "Cognitive", "Deign", "Fervid", "Gall", "Levee", "Preternatural", "Quell", "Score (n)", "Abut", "Consternation", "Gavel", "Lien", "Parenthesis", "Sinewy", "Steep (v)", "Tamp", "Venturing", "Wry", "Arduous", "Decimated", "Fledge", "Gouge", "Picayune", "Riveting", "Soliloquy", "Supplicant", "Transcendental", "Veritable", "Condescension", "Divest", "Eddy", "Epaulet", "Fallacy", "Fringe", "Leaven", "Patronize", "Prominent", "Statute", "Antipathy", "Aver", "Expatiate", "Flag (v)", "Flail", "Indicted", "Loll", "Malign", "Secure (v)", "Talon", "Abeyance", "Disarm", "Elaborate", "Foment", "Jockeying", "Minutiae", "Rue", "Somatic", "Stinting", "Temperate", "Allure", "Caulk", "Conscript", "Desultory", "Elegy", "Fallow", "Forbearing", "Hegemony", "Improbity", "Qualm", "Assay", "Chauvinist", "Discrete", "Enlist", "Fabricated", "Fulminate", "Hawser", "Jibe", "Peer", "Stickler", "Cloture", "Congruent", "Dally", "Dissemble", "Dote", "Errant", "Fervent", "Stomach (v)", "Synapse", "Undercutting", "Arson", "Carrion", "Intelligible", "Ironclad", "Lint", "Pretension", "Pundit", "Pyre", "Sate", "Syncopation", "Abraded", "Apposite", "Diatribe", "Gerontocracy", "Maculated", "Quisling", "Sedulity", "Seine", "Tender", "Waffle", "Burlesque", "Exemplar", "Homiletics", "Impugn", "Incubus", "Lope", "Macerate", "Nostrum", "Saw", "Sibyl", "Brook", "Emboss", "Eschew", "Limpid", "Liturgy", "Nexus", "Odometer", "Purchase", "Quotidian", "Seminal", "Agog", "Amortize", "Curmudgeon", "Dormancy", "Efficacy", "Epithet", "Figurehead", "Fracas", "Jamb", "Milk", "Chorales", "Dissonance", "Frieze", "Gist", "Latent", "Partiality", "Plodding", "Rekindle", "Symphony", "Tarnished", "Compromised", "Drabness", "Endow", "Esoterica", "Falters", "Prattle", "Prohibitive", "Purist", "Quack", "Taunt", "Arresting (a)", "Barrage", "Chantey", "Ferrous", "Manipulative", "Orate", "Psychosis", "Savor", "Table (v)", "Underwrite", "Dissident", "Enigmatic", "Foolhardy", "Homogeneity", "Personification", "Plaque", "Plausibility", "Resilience", "Trilogy", "Vagary", "Aisle", "Discountenance", "Imperative", "Indigent", "Nadir", "Paranoia", "Prudence", "Resuscitation", "Shirk", "Teetotalism", "Balm", "Calibrate", "Cataclysmic", "Impropriety", "Pith", "Primordial", "Reconnaissance", "Sinistral", "Tempers", "Undermine"





]
#"Abhor", "Bigot", "Counterfeit", "Enfranchise", "Hamper", "Kindle", "Noxious", "Placid", "Remuneration", "Talisman", "Abrasive", "Bilk", "Covert", "Engender", "Hangar", "Knotty", "Nuance", "Plagiarism", "Renown", "Tangent", "Abasement", "Billowing", "Cower", "Enhance", "Harangue", "Labyrinth", "Nullify", "Plaintiff", "Replete", "Tangible", "Abrogate", "Blasphemy", "Credible", "Enigma", "Harbingers", "Labyrinthine", "Nuzzle", "Plaudit", "Reprehensible", "Tardy", "Absolution", "Blatant", "Ensconce", "Hasten", "Laceration", "Obdurate", "Plausible", "Reprieve", "Tawdry", "Abstain", "Blighted", "Credulous", "Haughtiness", "Lachrymose", "Obfuscate", "Plethora", "Repudiate", "Tedium", "Abstemious", "Blithe", "Crepuscular", "Enunciation", "Headstrong", "Lackluster", "Objective", "Pliable", "Rescind", "Temper", "Abstruse", "Blunderbuss", "Cringe",
#  "Hedonism", "Laconic", "Oblique", "Plumage", "Resignation", "Tenacious", "Accolade", "Bolster", "Cryptic", "Ephemeral", "Hedonist", "Lamentation", "Obliterate", "Plummet", "Resolution", "Tentative", "Acquiesce", "Bombast", "Curtail", "Epicure", "Heed", "Lampoon", "Oblivious", "Podium", "Resonant", "Tenuous", "Acrid", "Boorish", "Cynical",
#  "Heresy", "Lance", "Obscure", "Poignant", "Respite", "Terse", "Acrophobia", "Bourgeois",
#  "Epistolary", "Hiatus", "Languid", "Obscured", "Poised", "Resplendent", "Therapeutic", "Acuity", "Braggart",
#, "Creditable", "Enshroud""Envenom","Epistle","Debility","Debunking",
k=0
#f = open('vocabulary.txt','w')

for each in list:
    try:
        url=("https://www.vocabulary.com/dictionary/"+(each))
        list = requests.get(url).text
        soup = BeautifulSoup(list, "html.parser")
        word = soup.find("h1", {"class": "dynamictext"})
        print(word.get_text())
        primaryMeaning = soup.find("p",{"class":"short"})
        print(primaryMeaning.get_text())
        secondaryMeaning = soup.find("p",{"class":"long"})
        print(secondaryMeaning.get_text())
        example = soup.findAll("div",{"class":"example"})
        #mean = soup.findAll("h3",{"class":"definition"})
        for i in example:
            #print(mean.get_text())
            print(i.get_text(), end=" ")
        print("\n\n-------------------------------------------")
    except:
        print(each)
        continue

for i in list:
    print(i,end="       ")