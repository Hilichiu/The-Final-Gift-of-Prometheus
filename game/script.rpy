# -- 0. Set Default Audio Volumes --
# This runs at the start of the game.
init python:
    # Sets the default volume for the 'music' (BGM) mixer to 70%
    _preferences.set_volume("music", 0.5)
    
    # Sets the default volume for the 'sound' (SFX) mixer to 100%
    _preferences.set_volume("sound", 0.8)

    # Sets the default volume for the 'video' (Movie) mixer to 100%
    _preferences.set_volume("video", 1.0)

# -- 1. Character Definitions -------------------------------------------------

define n = Character(None)
define p = Character("Prometheus", color="#FFD700") # Golden text
define h = Character("Honoka", color="#FF4500")      # Fiery orange text
define k = Character("Kaito", color="#228B22")      # Forest green text
define y = Character("Yui", color="#9370DB")        # Lavender text
define o = Character("Orcade", color="#8B4513")      # Muddy brown text

# -- 1b. Custom Position Definitions ------------------------------------------

define farleft = Position(xalign=0, yalign=1.0)
define farright = Position(xalign=1, yalign=1.0)

# -- 1c. Custom Transitions ---------------------------------------------------
# CORRECTED: Added the missing definition for the 'flash' transition.
# This fades to white for 0.1s, holds (for 0.0s), then fades in for 0.1s.
define flash = Fade(0.1, 0.0, 0.1, color="#ffffff")


# -- 2. Image and Audio Definitions -------------------------------------------

# Backgrounds
image bg mountain peak day = "images/bg_mountain_peak_day.png"
image bg mountain path day = "images/bg_mountain_path_day.png"
image bg mountain peak view = "images/bg_mountain_peak_view.png"
image bg mountain peak night = "images/bg_mountain_peak_night.png"
image bg clearing day = "images/bg_clearing_day.png"
image bg black = "images/bg_black.png"
image bg light wave = "images/bg_light_wave.png"

# Characters
image p chained suffering = "images/p_chained_suffering.png"
image p chained coma = "images/p_chained_coma.png"
image p unconscious ground = "images/p_unconscious_ground.png"
image p glowing standing = "images/p_glowing_standing.png"
image p glowing smile = "images/p_glowing_smile.png"
image p glowing fading = "images/p_glowing_fading.png"

image h normal = "images/h_normal.png"
image h determined = "images/h_determined.png"
image h shocked = "images/h_shocked.png"
image h battle fire = "images/h_battle_fire.png"
image h idea = "images/h_idea.png"
image h crying = "images/h_crying.png"

image k normal = "images/k_normal.png"
image k guard = "images/k_guard.png"
image k shocked = "images/k_shocked.png"
image k determined = "images/k_determined.png"
image k bow = "images/k_bow.png"

image y normal = "images/y_normal.png"
image y scared = "imagesTwo/y_scared.png"
image y horrified = "images/y_horrified.png"
image y healing = "images/y_healing.png"
image y crying = "images/y_crying.png"

image o normal = "images/o_normal.png"
image o roaring = "images/o_roaring.png"
image o laughing = "images/o_laughing.png"
image o angry = "images/o_angry.png"
image o rage = "images/o_rage.png"
image o pain = "images/o_pain.png"
image o dissolving = "images/o_dissolving.png"

image orc guard = "images/orc_guard.png"
image eagle = "images/eagle.png"

# Special Effects
image vfx explosion = "images/vfx_explosion.png"
image vfx lace barrier = "images/vfx_lace_barrier.png"
image vfx comet fist = "images/vfx_comet_fist.png"
image vfx leg fire = "images/vfx_leg_fire.png"
image vfx prometheus lightwave = "images/vfx_prometheus_lightwave.png"

# Audio
define audio.bgm_torment = "audio/bgm_torment.mp3"
define audio.bgm_journey = "audio/bgm_journey.mp3"
define audio.bgm_tension = "audio/bgm_tension.mp3"
define audio.bgm_rescue = "audio/bgm_rescue.mp3"
define audio.bgm_boss_battle = "audio/bgm_boss_battle.mp3"
define audio.bgm_climax = "audio/bgm_climax.mp3"
define audio.bgm_farewell = "audio/bgm_farewell.mp3"

# -- 3. The Script ------------------------------------------------------------

label start:

    # -- Scene 1: The Mountain of Torment --

    scene bg mountain peak day with fade
    play music "audio/bgm_torment.mp3" loop

    show p chained suffering at center
    show eagle at center
    n "Prometheus gave fire to man. For this, Zeus chained him to a mountain for endless torment. But on the first day, a new evil found him."

    show o normal at left with easeinleft
    
    play sound "audio/sfx_rock_throw.wav"
    hide eagle with dissolve
    play sound "audio/sfx_eagle_shriek.wav"
    
    o "(Sniffing the air) Fresh meat. Endless. This mountain is ours. This feast... is *ours*!"
    
    show o roaring at left
    play sound "audio/sfx_orc_roar_deep.wav"
    pause 1.0
    hide o roaring
    show o normal at left
    
    # Simple screen shake for Prometheus's scream
    p "AAAAARGH!" with vpunch
    play sound "audio/sfx_prometheus_scream.wav"

    scene bg black with fade

    # -- Scene 2: The Trembling Path --

    scene bg mountain path day with fade
    play music "audio/bgm_journey.mp3" loop

    show h normal at left
    show k normal at center
    show y normal at right
    
    n "29 days later. Three heroes passed nearby on their journey."
    
    stop music fadeout 1.0
    play music "audio/bgm_tension.mp3" loop
    
    # Ground shaking effect
    play sound "audio/sfx_ground_shake.wav" loop
    show h normal at left with {'xalign':0.25, 'yalign':1.0, 'linear':0.1, 'xalign':0.24, 'yalign':1.0, 'linear':0.1, 'repeat':3}
    show k normal at center with {'xalign':0.5, 'yalign':1.0, 'linear':0.1, 'xalign':0.51, 'yalign':1.0, 'linear':0.1, 'repeat':3}
    show y normal at right with {'xalign':0.75, 'yalign':1.0, 'linear':0.1, 'xalign':0.74, 'yalign':1.0, 'linear':0.1, 'repeat':3}
    pause 1.0
    stop sound
    
    h "Whoa! What's that shaking?"
    
    show k guard at center
    play sound "audio/sfx_sword_draw.wav"
    k "Not an earthquake. It's... footsteps. Heavy footsteps. From up there."
    
    show y scared at right
    y "L-look! Smoke! And... screaming. It sounds so p-painful."
    
    show h determined at left
    h "I’ve got a bad feeling. Let's go!"
    
    hide h determined
    hide k guard
    hide y scared
    
    scene bg mountain peak view with dissolve
    n "The heroes climbed the peak. What they saw was a nightmare."
    n "The great Titan Prometheus was surrounded by orcs, led by Orcade, who feasted on him."
    
    scene bg mountain path day with dissolve
    show h shocked at left
    show k shocked at center
    show y horrified at right
    
    y "They're... they're *eating* him... It's horrible."
    
    show k determined at center
    k "That's Prometheus. The one who gave us fire."
    
    show h determined at left
    h "We *have* to save him. We can't fight them all in the day. We wait for night."
    
    k "Agreed. Honoka, you create a distraction. Yui, you get to Prometheus. I'll cover you both. We strike fast, and we get him out."
    
    stop music fadeout 1.0
    
    scene bg black with fade
    
    # -- INTRO VIDEO --
    
    $ renpy.movie_cutscene("intro.webm")

    # -- Scene 3: The Night Rescue --

    scene bg mountain peak night with fade
    play music "audio/bgm_rescue.mp3" loop
    
    show p chained coma at center
    show o normal at farleft
    show orc guard at right
    show orc guard at farright
    
    n "As darkness fell, the rescue began."
    
    # Honoka is off-screen
    h "HEY, UGLY! DINNER'S OVER!"
    
    play sound "audio/sfx_explosion_loud.wav"
    show vfx explosion at center with hpunch
    pause 0.5
    hide vfx explosion
    
    play sound "audio/sfx_orc_roar_small.wav"
    hide orc guard with easeoutright
    hide orc guard with easeoutright
    
    show o roaring at farleft
    play sound "audio/sfx_orc_roar_deep.wav"
    o "INTRUDERS! FIND THEM! KILL THEM!"
    
    hide o roaring with easeoutleft
    
    show k guard at right with easeinright
    show y healing at farright with easeinright

    k "Yui, now!"
    
    play sound "audio/sfx_chain_break.wav"
    show k guard at right with vpunch
    
    show y healing at center with move
    
    play sound "audio/sfx_heal_chime.wav"
    show vfx lace barrier at center
    y "Lace Cloister Circle!"
    pause 1.0
    hide vfx lace barrier
    
    y "He's so weak... he's in a coma."
    
    k "We have to move!"
    
    show o angry at left with easeinleft
    o "THIEVES! You steal my FEAST!"
    
    k "Go! I'll hold him!"
    
    play sound "audio/sfx_axe_swing.wav"
    play sound "audio/sfx_axe_block.wav"
    show k guard at right with hpunch
    
    k "RUN!"
    
    hide y healing with easeoutright
    hide k guard with easeoutright
    # Implies Honoka and Yui drag Prometheus
    hide p chained coma with easeoutright
    
    hide o angry with easeoutleft
    
    scene bg black with fade
    
    # -- Scene 4: The Final Stand --
    
    scene bg clearing day with fade
    play music "audio/bgm_boss_battle.mp3" loop
    
    # Prometheus is on the ground, Yui is healing him.
    show p unconscious ground at center
    show y healing at center
    
    show h battle fire at left
    show k guard at right
    
    n "The next morning, at the base of the mountain..."
    
    show o angry at farleft with easeinleft
    play sound "audio/sfx_orc_roar_deep.wav"
    
    o "NOWHERE TO RUN, LITTLE HUMANS. GIVE ME THE TITAN."
    
    h "You'll have to go through us! Blazing Comet Fist!"
    
    # Animate the fireball moving from left to farleft
    show vfx comet fist at left with {'xalign':0.25, 'linear':0.3, 'xalign':0.1}
    play sound "audio/sfx_fireball_whoosh.wav"
    play sound "audio/sfx_fire_impact_dull.wav"
    
    show o laughing at farleft
    o "Pathetic. Your fire is like a spark."
    
    show k guard at right
    k "Honoka, his skin is too thick! But look at his legs! Those guards... they're made of **wood**!"
    
    show h idea at left
    h "Wood? Got it! Time to light a fire!"
    
    # Honoka dashes
    show h battle fire at left with move
    show h battle fire at farleft
    play sound "audio/sfx_fireball_whoosh.wav" # Using this for her glide
    
    play sound "audio/sfx_fire_crackle.wav"
    show vfx leg fire at farleft # Overlay on Orcade
    
    show o pain at farleft
    o "WITCH! You'll pay!"
    
    hide vfx leg fire
    
    show o rage at farleft
    n "The leg guards burn away. He stumbles, now hurt and vulnerable. He goes into a 'Berserker Rage'!"
    
    play sound "audio/sfx_axe_swing.wav"
    show o rage at center with move
    
    # Knocking heroes down
    play sound "audio/sfx_body_thud.wav"
    show h battle fire at left with vpunch
    show k guard at right with vpunch
    
    hide h battle fire
    hide k guard
    
    show o rage at center
    o "BREAK!"
    
    show y scared at center
    y "NO!"
    
    stop music fadeout 1.0
    play sound "audio/sfx_divine_chime.wav"
    play music "audio/bgm_climax.mp3"
    
    scene bg light wave with flash # This line will now work
    
    scene bg clearing day
    show h shocked at left
    show k shocked at right
    show y scared at center
    
    show p glowing standing at center
    
    p "...Enough."
    
    h "Prometheus... You're awake!"
    
    show p glowing smile at center
    p "For centuries, I suffered. But you came for me. You... with my fire in your heart."
    p "You... with the strength to protect others."
    p "And you... with a kind heart to heal."
    
    show y crying at center
    y "But... you're... you're disappearing!"
    
    show p glowing standing at center
    p "My torment is over. My body is broken. But my spirit has one last gift to give."
    
    show o angry at farright
    p "My soul... for your future."
    
    play sound "audio/sfx_light_wave.wav"
    show vfx prometheus lightwave at center with hpunch
    
    scene bg light wave with flash # This line will also work
    
    show o dissolving at farright
    o "NO! IMPOSSIBLE...!"
    hide o dissolving with dissolve
    
    scene bg clearing day
    
    show p glowing fading at center
    show k bow at left
    show h crying at right
    show y crying at center
    
    k "We... we are honored."
    
    h "Don't go! We promise to keep your fire safe!"
    
    p "You already are... Live well, children of my fire..."
    
    hide p glowing fading with dissolve
    play sound "audio/sfx_wind_whisper.wav"
    
    stop music fadeout 2.0
    play music "audio/bgm_farewell.mp3" loop
    
    n "And so, the torment of Prometheus ended. Not by a god, but by the courage, kindness, and fire of humanity."
    n "His spirit was, at last, free."
    
    show h determined at left
    show k normal at center
    show y normal at right
    
    n "Honoka, Kaito, and Yui stand together, looking up."
    
    scene bg black with fade
    
    n "THE END (Prometheus Route)"

    return