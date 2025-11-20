# Dialogue Extraction Status Report
*Updated: 2025-11-20*

---

## Overview Statistics

| Category | Count |
|----------|-------|
| **Total Gale HTML source files** | 59 |
| **Total Astarion HTML source files** | 54 |
| **Total HTML source files** | 113 |
| **Extracted Gale dialogues** | 91 |
| **Extracted Astarion dialogues** | 84 |
| **Total extracted files** | 175 |
| **Estimated completion** | ~90-95% |

---

## Recently Completed (Since Last Update)

### Latest Batch (Current Session)
- **Gale World Reactions:**
  - `gale_druid_grove_world_reactions.md` - Combined Nettie poison, harpy child, Kagha snake reactions
  - `gale_astarion_reveal_reaction_2.md` - Origin-specific voluntary confession path
- **Astarion:**
  - `astarion_controlling_tadpole.md` - Tadpole power scheme discussion
- **Cross-Character References:**
  - `karlach_reactions_to_astarion.md` - Bite confrontation and confession reactions

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

- [x] Druid Grove world reactions (Nettie poison, harpy child, Kagha snake)
- [x] Cross-character reactions (Astarion reveal origin path)

#### Partially Extracted / Needs Review
- [ ] Main hub residuals (`Gale_InParty2.html` - core content extracted via nested files)

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
- [x] Controlling tadpole power scheme discussion
- [x] Cross-character references (Karlach bite/confession reactions)

#### Partially Extracted / Needs Review
- [ ] Main hub residuals (`Astarion_InParty2.html` - core content extracted via nested files)
- [ ] Spare phrases (nested file - low priority, generic barks)

#### To Skip (Technical/Test)
- `Astarion_InPartyEND.html` - End state template
- `CC_Astarion_Intro.html` - Character creation

---

## Remaining Work

### Completed This Session
- ~~World Reaction Dialogues (Gale)~~ → `gale_druid_grove_world_reactions.md`
- ~~Controlling Tadpole~~ → `astarion_controlling_tadpole.md`
- ~~Cross-Character References~~ → `karlach_reactions_to_astarion.md`, `gale_astarion_reveal_reaction_2.md`

### Low Priority (Optional Cleanup)
1. **InParty2 Hub File Review:**
   - Check both `Gale_InParty2.html` and `Astarion_InParty2.html` for any content not covered by nested file extractions
   - *Note: All significant nested content has been extracted*

2. **Spare Phrases:**
   - `Astarion_InParty2_Nested_SparePhrases.html` - Generic barks, likely low value

3. **Origin-Specific Files (Already Reviewed):**
   - `ORI_Astarion_PAD_VampiricNatureDiscussion.html` - Contains only other-companion dialogue
   - `GLO_Astarion_PAD_AstarionKidnapped.html` - Core content already in `astarion_kidnapped.md`

---

## Summary

The extraction work is approximately **90-95% complete**. All major story beats, character arcs, and pivotal moments have been captured for both Gale and Astarion. The remaining items are low-priority optional cleanup:

- **Hub file residuals** (likely nothing significant remaining)
- **Generic spare phrases** (barks and filler dialogue)

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
