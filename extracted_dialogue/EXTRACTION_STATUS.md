# Dialogue Extraction Status Report
*Updated: 2025-11-20*

---

## Overview Statistics

| Category | Count |
|----------|-------|
| **Total Gale HTML source files** | 59 |
| **Total Astarion HTML source files** | 54 |
| **Total HTML source files** | 113 |
| **Extracted Gale dialogues** | 89 |
| **Extracted Astarion dialogues** | 82 |
| **Total extracted files** | 171 |
| **Estimated completion** | ~85-90% |

---

## Recently Completed (Since Last Update)

### Gale - Major Additions
- **Epilogues:** `gale_epilogue.md`, `gale_tara_epilogue.md`, `gale_romance_morning_after.md`
- **Elminster Encounters:**
  - `elminster_mystras_summons_gale_alone.md`
  - `elminster_mystras_summons_with_party.md`
  - `elminster_returns_gale_alone.md`
  - `elminster_returns_with_companions.md`
  - `elminster_visit_mystras_command.md`
- **Origin/Death Mechanics:**
  - `gale_death_flute_and_mephit.md`
  - `gale_death_pouch.md`
  - `gale_death_lava_scroll.md`
  - `gale_death_resurrection_reminders.md`
  - `gale_orb_worsening_urgent.md`
  - `gale_orb_discomfort_barks.md`
- **Mystra's Shrine:** `gale_mystras_shrine.md`, `gale_mystra_tabernacle.md`

### Astarion - Complete Coverage
- **Epilogues:** 6 distinct ending variations fully extracted
- **Camp Nights:** All three nights complete
- **Romantic Arc:** Full progression from first night through real connection confession
- **Cazador Confrontation:** Complete palace, ritual room, and spawn resolution coverage
- **All Banter:** Complete with Gale, Karlach, Wyll companions

---

## Extraction Completion by Category

### GALE

#### Fully Extracted
- [x] Recruitment and early game
- [x] Magic item consumption arc (all three items)
- [x] Orb/Mystra revelation arc
- [x] Spell teaching conversations
- [x] Tara encounters (all scenes including posthouse, camp join, epilogue)
- [x] Elminster encounters (Act 2 and Act 3)
- [x] Crown of Karsus discussion
- [x] Last Night Alive (all variations)
- [x] God proposal rejection
- [x] Orin abduction
- [x] Epilogue (main + Tara)
- [x] All companion banter (Astarion, Lae'zel, Shadowheart, Karlach, Wyll, Jaheira, Minsc, Minthara)
- [x] Topical greetings (extensive coverage across acts)
- [x] Origin death mechanics (death pouch, flute, resurrection, orb warnings)
- [x] Endgame conversations
- [x] Tiefling celebration (all variations)

#### Partially Extracted / Needs Review
- [ ] Main hub residuals (`Gale_InParty2.html` - core content extracted via nested files)
- [ ] World reactions: `DEN_Apprentice_WRD_Gale.html`, `DEN_HarpyMeal_WRD_Gale.html`, `DEN_ShadowDruid_WRD_Gale.html`

#### To Skip (Technical/Test)
- `Gale_InPartyEND.html` - End state template
- `Gale_InPartyTemplateTest.html` - Test file
- `Gale_Recruitment2.html` - Duplicate
- `Gale_IPRDs.html`, `Gale_IPRDs2.html`, `Gale_IPRDs3.html` - Random dialogues (key content already extracted)

---

### ASTARION

#### Fully Extracted
- [x] Character introduction/recruitment
- [x] Camp nights 1, 2, 3
- [x] Vampire reveal and confrontation
- [x] Cazador backstory revelation
- [x] Gur Hunter encounters
- [x] Raphael scars revelation
- [x] Tasting party
- [x] Black Mass aftermath
- [x] Blood merchant aftermath
- [x] Romance arc (all stages through real connection)
- [x] Partnered conversations (kisses, protection, "what are we", breakup option)
- [x] Sebastian spawn
- [x] Tadpole powers discussion
- [x] Dangerous book
- [x] Infernal vendor
- [x] Gur camp and followup
- [x] Cazador's palace (kennel, cells, in-palace reactions)
- [x] Ritual room (precombat and postcombat spawn path)
- [x] Vampire spawns resolution
- [x] Kidnapped scenario
- [x] All six epilogue variations
- [x] All companion banter (Gale, Karlach, Wyll)
- [x] Extensive topical greetings (all acts)
- [x] Endgame conversations

#### Partially Extracted / Needs Review
- [ ] Main hub residuals (`Astarion_InParty2.html` - core content extracted via nested files)
- [ ] Controlling tadpole discussion (nested file)
- [ ] Spare phrases (nested file)

#### To Skip (Technical/Test)
- `Astarion_InPartyEND.html` - End state template
- `CC_Astarion_Intro.html` - Character creation

---

## Remaining Work

### High Priority (Story Content Gaps)
1. **World Reaction Dialogues (Gale):**
   - `DEN_Apprentice_WRD_Gale.html` - Apprentice reactions
   - `DEN_HarpyMeal_WRD_Gale.html` - Harpy feast reactions
   - `DEN_ShadowDruid_WRD_Gale.html` - Shadow Druid reactions
   - `DEN_CapturedGoblin_SteppedInFrontOfCrossbow_WRD_Gale.html` - Goblin crossbow anecdote

2. **InParty2 Hub File Review:**
   - Check both `Gale_InParty2.html` and `Astarion_InParty2.html` for any content not covered by nested file extractions

### Medium Priority (Additional Context)
3. **Astarion Nested Files:**
   - `Astarion_InParty2_Nested_ControllingTadpole.html`
   - `Astarion_InParty2_Nested_SparePhrases.html`

4. **Cross-Character References:**
   - `Karlach_InParty_Nested_AstarionBiteConfrontation.html`
   - `Karlach_InParty_Nested_AstarionConfession.html`
   - `Gale_InParty2_Nested_AstarionReveal2.html`

### Low Priority (Origin Mechanics)
5. **Origin-Specific Files:**
   - `ORI_Astarion_PAD_VampiricNatureDiscussion.html`
   - `GLO_Astarion_PAD_AstarionKidnapped.html`

---

## Summary

The extraction work is approximately **85-90% complete**. All major story beats, character arcs, and pivotal moments have been captured for both Gale and Astarion. The remaining work consists primarily of:

- **World reaction dialogues** (minor flavor content)
- **Hub file residuals** (content not covered by nested extractions)
- **Cross-character references** (Karlach reactions to Astarion events)
- **Origin-specific mechanics** (lower priority)

### What's Fully Done
- Complete romantic arcs for both characters
- All major story confrontations (Mystra, Cazador)
- All epilogue variations
- Complete companion banter
- Extensive topical greetings
- All Elminster encounters
- All Tara encounters
- Death/resurrection mechanics

The Lore Lexicon now has comprehensive coverage of Gale and Astarion's narrative content across all three acts and the epilogue.

---

*End of Report*
