# Dialogue Extraction Status Report
*Generated: 2025-11-19*

---

## Overview Statistics

| Category | Count |
|----------|-------|
| **Total Gale HTML files** | 59 |
| **Total Astarion HTML files** | 55 |
| **Total HTML files** | 114 |
| **Extracted Gale dialogues** | ~50 |
| **Extracted Astarion dialogues** | ~60 |
| **Remaining to extract** | ~50-60 files |

---

## GALE: Unextracted Files

### High Priority - Main Story Dialogues

#### InParty2 Base & Nested Files
- `Gale_InParty2.html` - **Main dialogue hub** (critical)
- `Gale_InParty2_Nested_ShadowheartShar.html` - Shadowheart/Shar reactions
- `Gale_InParty2_Nested_TopicalGreetings.html` - Context-specific greetings
- `Gale_InParty2_Nested_AdditionalGreetings.html` - More contextual greetings

#### Act 2 - Elminster Encounters
- `GLO_Elminster_OM_Gale_COM.html` - Elminster companion reactions
- `GLO_Elminster_OM_Gale_AOM_OOM.html` - Elminster avatar/origin reactions
- `GLO_Elminster_CFM_GaleAlone.html` - Elminster (Gale alone)
- `GLO_Elminster_CFM_GaleCom.html` - Elminster companion mode
- `LOW_Elminster_OM_Gale_COM.html` - Lower City Elminster reactions
- `LOW_Elminster_OM_Gale_AOM_OOM.html` - Lower City Elminster avatar/origin

#### Act 2 - Mystra's Shrine (Stormshore Tabernacle)
- `LOW_StormshoreTabernacle_MystraShrine_OM_Gale_COM.html` - Shrine reactions

#### World Reactions (Wilderness/Underdark/Rosymorn)
- `WYR_Posthouse_GalesTressym_OM_Gale_AOM_COM_OOM.html` - Tara at posthouse
- `DEN_ShadowDruid_WRD_Gale.html` - Shadow Druid reactions
- `DEN_HarpyMeal_WRD_Gale.html` - Harpy feast reactions
- `DEN_Apprentice_WRD_Gale.html` - Apprentice reactions
- `DEN_CapturedGoblin_SteppedInFrontOfCrossbow_WRD_Gale.html` - Goblin crossbow scene

#### Epilogue
- `EPI_Epilogue_Gale.html` - **Epilogue party dialogue**
- `EPI_Epilogue_Tara.html` - **Tara's epilogue dialogue**

#### Endgame
- `END_IllithidOptions_WRD_GaleBombOption.html` - Illithid endgame bomb choice

---

### Origin/Death Mechanics (Lower Priority)
- `ORI_Gale_PAD_DeathNoteLava.html` - Origin death note (lava)
- `ORI_Resurrected_WRD_Gale.html` - Resurrection reactions
- `ORI_Gale_Deathvoice_Reminder.html` - Death voice reminder
- `ORI_Gale_DeathPouch.html` - Death pouch dialogue
- `ORI_Gale_DeathFlute.html` - Death flute dialogue
- `ORI_Gale_AvatarStrengthens.html` - Avatar strengthening
- `ORI_Gale_AD_AvatarWorsens.html` - Avatar worsening
- `ORI_Gale_AD_BombComplain.html` - Bomb complaints
- `ORI_Gale_AD_AvatarStrengthens.html` - Avatar strengthens (AD)
- `Gale_DeathVoice.html` - Death voice main
- `Gale_DeathVoice_StatusFallback.html` - Death voice fallback
- `Gale_AD_PreRecruitment.html` - Pre-recruitment autodialogues

---

### Technical/Test Files (Skip)
- `Gale_InPartyTemplateTest.html` - Template test file
- `Gale_InPartyEND.html` - End state template
- `Gale_Recruitment2.html` - Duplicate/alternate recruitment
- `Gale_IPRDs.html` - In-party random dialogues (old)
- `Gale_IPRDs2.html` - In-party random dialogues 2
- `Gale_IPRDs3.html` - In-party random dialogues 3

---

### Special Events
- `CAMP_OrinAbduction_CFM_Gale.html` - **Already extracted** ✓
- `CAMP_Gale_CRD_ROM_BeMyGod.html` - **Already extracted** (god proposal rejection) ✓

---

## ASTARION: Unextracted Files

### High Priority - Main Story Dialogues

#### InParty2 Base & Main Nested Files
- `Astarion_InParty2.html` - **Main dialogue hub** (critical)
- `Astarion_InParty2_Nested_TopicalGreetings.html` - Context-specific greetings
- `Astarion_InParty2_Nested_SparePhrases.html` - Additional dialogue phrases
- `Astarion_InParty2_Nested_ControllingTadpole.html` - Tadpole control discussion

#### Camp Conversations
- `CAMP_Night1_CRD_Astarion.html` - Night 1 camp conversation
- `CAMP_Night2_CRD_Astarion.html` - Night 2 camp conversation
- `CAMP_Night3_CRD_Astarion.html` - Night 3 camp conversation
- `CAMP_GoblinHuntRaiderCelebration_CRD_Astarion.html` - Raider celebration
- `CAMP_GoblinHuntTieflingCelebration_CRD_Astarion.html` - Tiefling celebration

#### Act 3 - Cazador's Palace (Additional)
- Note: Several palace files already extracted, but verify coverage

---

### Cross-Character References

#### In Other Character Files
- `Gale_InParty2_Nested_AstarionReveal.html` - **Already extracted** ✓
- `Gale_InParty2_Nested_AstarionReveal2.html` - Gale's reactions to Astarion (may need review)
- `Karlach_InParty_Nested_AstarionConfession.html` - Karlach's reaction to confession
- `Karlach_InParty_Nested_AstarionBiteConfrontation.html` - Karlach bite confrontation

---

### Recruitment & Early Game
- `Astarion_Recruitment.html` - Initial recruitment (may already be covered)

---

### Origin/PAD Files (Lower Priority)
- `ORI_Astarion_PAD_VampiricNatureDiscussion.html` - Vampiric nature discussion
- `GLO_Astarion_PAD_AstarionKidnapped.html` - Kidnapping PAD

---

### Technical/Test Files (Skip)
- `Astarion_InPartyEND.html` - End state template
- `CC_Astarion_Intro.html` - Character creation intro

---

## Extraction Priority Recommendations

### IMMEDIATE (Critical Story Content)

**Gale:**
1. `Gale_InParty2.html` - Main dialogue hub
2. `EPI_Epilogue_Gale.html` - Epilogue party
3. `EPI_Epilogue_Tara.html` - Tara's epilogue
4. Elminster encounter files (6 files total)
5. `LOW_StormshoreTabernacle_MystraShrine_OM_Gale_COM.html`

**Astarion:**
1. `Astarion_InParty2.html` - Main dialogue hub
2. Camp night conversations (Night 1, 2, 3)
3. Celebration files (raider + tiefling)

### MEDIUM PRIORITY (Context & World Reactions)

**Gale:**
- Nested topical greetings (2 files)
- World reaction dialogues (DEN_ prefix files)
- `WYR_Posthouse_GalesTressym_OM_Gale_AOM_COM_OOM.html`

**Astarion:**
- Nested topical greetings and spare phrases
- Tadpole control discussion
- Cross-character references (Karlach files)

### LOW PRIORITY (Origin/Mechanics)

**Both Characters:**
- Origin-specific files (ORI_ prefix)
- Death mechanics and voices
- PAD (Player Avatar Dialogue) files for origin runs
- Technical/template files

---

## Files to SKIP Entirely

### Test/Technical Files
- `*_InPartyEND.html` - Template end states
- `*_InPartyTemplateTest.html` - Test files
- `*_IPRDs.html` - Old random dialogue systems
- `CC_*_Intro.html` - Character creation screens

### Duplicate/Alternate Versions
- `Gale_Recruitment2.html` (if Recruitment.html already extracted)

---

## Extraction Notes

### Already Completed
- **Gale Act 1:** Most camp scenes, magic item arcs, major story beats ✓
- **Gale Act 2:** Elminster visit, Crown of Karsus, Last Night Alive, Tara scenes ✓
- **Gale Act 3:** God proposal rejection, Orin abduction ✓
- **Astarion Act 1:** Extensive romantic arc, Cazador backstory, Raphael interactions ✓
- **Astarion Act 2:** Some world reactions ✓
- **Astarion Act 3:** Cazador palace confrontation, ritual resolution, spawn choice ✓
- **Astarion Epilogue:** Multiple ending variations ✓

### Gap Analysis
The main gaps are:
1. **InParty2.html hub files** for both characters (major dialogue hubs)
2. **Elminster encounters** for Gale (6 files across acts)
3. **Early camp conversations** for Astarion (nights 1-3)
4. **Epilogue** for Gale (both Gale and Tara)
5. **Contextual greetings and reactions** scattered across both

---

## Next Steps

1. **Extract Gale & Astarion InParty2.html files first** - These are the main dialogue hubs
2. **Epilogue files** - Critical story closure
3. **Elminster encounters** - Major Act 2 story beats
4. **Early camp conversations** - Character establishment
5. **World reactions and greetings** - Context and flavor

The extraction work is approximately **50-60% complete**, with most major story beats captured but significant gaps in hub dialogues, epilogues, and contextual reactions.

---

*End of Report*
