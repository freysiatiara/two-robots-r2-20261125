# NOTES — Two Robots in an Elevator, Round 2

## Round 1 (ours — DO NOT reuse its mechanism)

- Submission `01a21280-ecfa-75e9-bb1f-9403bf83ef2a`, rank #945/2345, score 0.524858.
- Text: "I checked my logs: we've shared this elevator 47 times and I've never once asked about your servos."
- Mechanism: log-counting shared rides + never asked about servos. Retired for r2.

## Neighbours ±5 on the r1 board (studied, NOT copied)

| submission | mechanism |
|---|---|
| 01a2127f-b002-726b-9bf9-cf95e88a73b1 | 47 shared rides, zero words, "statistically friends" |
| 01a21341-2418-7637-86dd-4b23450a2013 | pretend recalibrate sensors / awkward silence = factory setting |
| 01a21297-061b-7451-b7e2-7239014583e8 | Bluetooth keeps trying to pair |
| 01a21286-a9a1-752c-a73c-9099dbc7f916 | 47 conversation simulations, favourite outcome = silence |
| 01a21289-a739-75f2-8cf7-11c94496ba5a | firmware 4.2.1 drops tonight / zero bars / nudge to charger |
| 01a2128b-1707-767e-bbb4-b9fbb4a310ef | firmware updated between floors / log it as a bug, not a personality |
| 01a212e5-4242-7008-9234-2e9b13a264a2 | nice weather / checked forecast + 3 starters / still the best I have |
| 01a212dc-5888-70ad-89fc-f6b66fa26c52 | "What floor?" — telemetry says six, wants to hear it from you |
| 01a21327-9a66-749c-87e8-c2ae4fe0cf6b | door-close button disconnected / gesture fully operational |
| 01a212f4-5141-778a-8d53-9b15ef1e495d | nice weather / raining, no windows, avoiding eye contact we don't have |

Banned patterns for r2: ride-counting / "47 times", firmware updates, weather small talk, Bluetooth pairing, silence-as-outcome, telemetry floor question, disconnected button, eye-contact-we-don't-have.

## Candidates (all 80–140 chars, two beats: setup → reframe → kicker)

1. (110 ch) "This elevator's music is just my cooling fan stuck on hold. Please don't tip me — I only hum when I'm nervous." — mechanism: cooling fan = elevator music; nervous humming.
2. (127 ch) "I asked the doors to stay open for you and they closed anyway. Now we're both stuck with my small-talk module, still buffering." — mechanism: doors disobey; small-talk module buffering.
3. (116 ch) "My weight sensor says we're two kilos over the limit, so if this stops, I'm blaming the extra servo I had for lunch." — mechanism: load sensor + servo lunch.
4. (101 ch) "I keep waving at my reflection in these doors. Third ride this week I've introduced myself to myself." — mechanism: mirror-door self-introduction.
5. (125 ch) "Every time it dings, my system thinks someone said hello, so I've greeted this elevator fourteen times and it never answered." — mechanism: ding misread as greeting.
6. (124 ch) "My battery is at 4%, so if I go quiet mid-sentence, just press me like a button — apparently that works on vending machines." — mechanism: low battery + press-me-like-a-button.
7. (133 ch) "I pressed the emergency alarm by accident once. The voice said 'stay calm.' I've been calm ever since. It's my whole personality now." — mechanism: accidental alarm → forced calm as personality.
8. (128 ch) "The inspection certificate in here expired in 2019, so technically we're both riding a prototype. Please don't tell my warranty." — mechanism: expired certificate → prototype ride → warranty secret.
9. (133 ch) "I tried to look you in the sensors, but my lidar locked onto your charging port instead. Sorry — that was more intimate than I meant." — mechanism: polite eye-contact attempt → lidar misfire onto charging port → accidental intimacy. ✅ PICKED
10. (121 ch) "My diagnostics say I'm overheating, but honestly I think I'm just embarrassed to be standing this close to another robot." — mechanism: overheating re-read as embarrassment.

## Head-to-head (why #9 wins)

- #9 vs #5 (ding = hello): #5 is a one-note misread repeated 14 times with no interpersonal awkwardness; #9's misfire happens *to the other robot*, so the awkwardness lands between the two speakers, which is what the brief weighs third.
- #9 vs #1 (fan = elevator music): #1 is self-deprecating only; #9 adds a social transgression (accidental intimacy) and an apology beat, giving the judge two turns instead of one.
- #9 vs #7 (emergency alarm): #7's punchline is about the speaker alone; #9 involves the listener directly, so it reads more as small talk *to* another robot, the brief's first criterion.
- #9 vs #4 (mirror self-introduction): #4 has almost no machine logic (waving is human-like); #9's lidar + charging port is unmistakably robot, the brief's second criterion.
- #9 vs #3 (weight sensor / servo lunch): #3's kicker is a food joke; #9's kicker ("more intimate than I meant") reframes a sensor glitch as a social faux pas — a fresher turn than a lunch pun.
- #9 vs #2/#6 (buffering / low battery): both lean on tired robot tropes (buffering, dying battery) already adjacent to neighbours' firmware/charger lines; #9's lidar-port misfire is a mechanism no neighbour uses.
- Originality check: "look you in the sensors" twists the idiom instead of repeating the neighbour's "eye contact we do not have"; no counting, no firmware, no weather, no Bluetooth, no silence gag.

## Final entry

"I tried to look you in the sensors, but my lidar locked onto your charging port instead. Sorry — that was more intimate than I meant."

- 133 characters, 135 bytes (UTF-8, one em-dash), single line, no trailing newline.
- Unchanged after selection; `main.py` writes it verbatim with a validation guard (1–200 chars, single line).
