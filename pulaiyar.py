from turtle import *
import time
import math

# ===== SETUP =====
title('🙏 CoderHuBhai - Ganesha Vinayak Chaturthi Animation 🙏')
bgcolor("black")
speed(0)

screen = getscreen()
screen.setup(1200, 900)

# Global position offset for movement animations
offset_x = 0
offset_y = 0

def CoderHu(x, y):
    """Move to position"""
    penup()
    goto(x + offset_x, y + offset_y)
    pendown()

# ===== COMPLETE GANESHA DRAWING FUNCTION =====
def draw_ganesha(pen_color='red', fill_color='orange', scale=1.0):
    """Draw complete Ganesha with optional color and scale"""
    pencolor(pen_color)
    fillcolor(fill_color)
    pensize(2)
    
    # trunk    
    CoderHu(-130, 150)
    seth(-120)
    begin_fill()
    circle(100, 90)
    circle(280, 10)
    circle(-120, 90)
    circle(-60, 150)
    circle(-30, 60)
    seth(-120)
    circle(30, 60)
    circle(55, 150)
    circle(120, 77)
    circle(-100, 115)
    end_fill()
    
    # chest
    CoderHu(0, 50)
    seth(20)
    begin_fill()
    circle(-50, 80)
    circle(-200, 70)
    circle(-50, 60)
    seth(-20)
    circle(50, 70)
    circle(205, 70)
    circle(50, 85)
    end_fill()
    
    # head
    CoderHu(70, 10)
    seth(15)
    begin_fill()
    circle(90, 120)
    seth(-52)
    circle(-90, 110)
    end_fill()

    # eyes
    def eye():
        seth(-55)
        begin_fill()
        circle(20, 120)
        seth(-90)
        circle(-17, 165)
        end_fill()
    
    CoderHu(-100, 110)    
    eye()
    CoderHu(40, 110)
    eye()

    # tilak (red mark on forehead)
    def cir(r):
        begin_fill()
        circle(r)
        end_fill()
    
    CoderHu(0, 150)    
    cir(10)
    CoderHu(-2, 125)
    cir(8)
    CoderHu(-4, 105)
    cir(5)

    # crown
    CoderHu(-80, 200)
    seth(30)
    begin_fill()
    circle(-150, 60)
    seth(141)
    circle(120, 80)
    end_fill()
    
    CoderHu(-70, 225)
    seth(30)
    begin_fill()
    circle(-120, 60)
    seth(141)
    circle(95, 80)
    end_fill()
    
    CoderHu(-30, 280)
    seth(-120)
    begin_fill()
    circle(20, 250)
    circle(-50, 40)
    seth(-100)
    circle(50, 42)
    circle(-15, 240)
    end_fill()
    
    CoderHu(-5, 268)
    cir(9)

    # left ear
    CoderHu(-160, 130)
    seth(120)
    begin_fill()
    circle(70, 60)
    circle(15, 100)
    circle(90, 30)
    circle(-15, 40)
    circle(90, 30)
    circle(20, 100)
    seth(-130)
    circle(-20, 100)
    circle(-90, 30)
    circle(15, 35)
    circle(-90, 50)
    circle(-18, 80)
    circle(-70, 80)
    end_fill()

    # right ear
    CoderHu(140, 130)
    seth(60)
    begin_fill()
    circle(-70, 60)
    circle(-15, 100)
    circle(-90, 30)
    circle(15, 40)
    circle(-90, 30)
    circle(-20, 100)
    seth(-50)
    circle(20, 100)
    circle(90, 30)
    circle(-15, 35)
    circle(90, 50)
    circle(18, 80)
    circle(70, 80)
    end_fill()

    # belly
    CoderHu(-130, -20)
    seth(-60)
    begin_fill()
    circle(-20, 60)
    circle(150, 50)
    circle(60, 60)
    seth(175)
    circle(-70, 70)
    circle(-132, 50)
    circle(40, 40)
    end_fill()

    # left leg
    CoderHu(-90, -250)
    seth(180)
    begin_fill()
    circle(-100, 60)
    circle(20, 90)
    circle(40, 40)
    circle(20, 60)
    circle(120, 40)
    seth(178)
    circle(-120, 40)
    circle(-25, 60)
    circle(-50, 50)
    circle(-30, 90)
    circle(70, 50)
    end_fill()

    # right leg
    CoderHu(120, -260)
    seth(15)
    begin_fill()
    circle(120, 50)
    circle(20, 90)
    circle(70, 40)
    circle(120, 40)
    circle(-60, 60)
    circle(70, 60)
    circle(20, 90)
    seth(-120)
    circle(20, 120)
    circle(40, 50)
    circle(-70, 40)
    seth(180)
    circle(65, 40)
    circle(-35, 40)
    circle(-17, 120)
    seth(120)
    circle(-14, 70)
    circle(-65, 60)
    circle(40, 70)
    circle(-115, 50)
    circle(-60, 20)
    circle(-15, 98)
    circle(-110, 50)
    end_fill()

    # left hand
    CoderHu(-170, -60)
    seth(180)
    begin_fill()
    circle(20, 80)
    circle(-30, 150)
    circle(20, 80)
    seth(0)
    circle(-20, 80)
    circle(32, 170)
    circle(-20, 80)
    end_fill()
    
    CoderHu(-205, -80)
    seth(75)
    begin_fill()
    circle(40, 60)
    seth(-150)
    circle(40, 60)
    seth(65)
    circle(-40, 40)
    seth(-45)
    circle(-40, 35)
    end_fill()

    # right hand
    CoderHu(240, -60)
    seth(180)
    begin_fill()
    circle(20, 80)
    circle(-30, 150)
    circle(20, 80)
    seth(0)
    circle(-20, 80)
    circle(32, 170)
    circle(-20, 80)
    end_fill()
    
    CoderHu(205, -80)
    seth(75)
    begin_fill()
    circle(40, 60)
    seth(-150)
    circle(40, 60)
    seth(65)
    circle(-40, 40)
    seth(-45)
    circle(-40, 35)
    end_fill()

# ===== ANIMATION 1: BLINKING =====
def blink_animation(times=4):
    """Eyes blinking animation"""
    print("👀 Animation 1: Eyes Blinking...")
    for i in range(times):
        # Closed eyes (line)
        clear()
        draw_ganesha()
        
        pencolor('red')
        pensize(5)
        CoderHu(-110, 110)
        seth(0)
        pendown()
        forward(25)
        penup()
        
        CoderHu(30, 110)
        seth(0)
        pendown()
        forward(25)
        penup()
        
        pensize(1)
        time.sleep(0.2)
        
        # Open eyes
        clear()
        draw_ganesha()
        time.sleep(0.35)
    
    print("   ✓ Blinking complete!")

# ===== ANIMATION 2: EYES WIDE OPEN (SURPRISED) =====
def wide_eyes_animation():
    """Wide open eyes surprised expression"""
    print("😮 Animation 2: Wide Open Eyes (Surprised)...")
    
    for cycle in range(2):
        # Wide open
        clear()
        pencolor('red')
        fillcolor('orange')
        
        # Draw body without eyes
        penup()
        goto(-130 + offset_x, 150 + offset_y)
        pendown()
        seth(-120)
        begin_fill()
        circle(100, 90)
        circle(280, 10)
        circle(-120, 90)
        circle(-60, 150)
        circle(-30, 60)
        seth(-120)
        circle(30, 60)
        circle(55, 150)
        circle(120, 77)
        circle(-100, 115)
        end_fill()
        
        CoderHu(0, 50)
        seth(20)
        begin_fill()
        circle(-50, 80)
        circle(-200, 70)
        circle(-50, 60)
        seth(-20)
        circle(50, 70)
        circle(205, 70)
        circle(50, 85)
        end_fill()
        
        CoderHu(70, 10)
        seth(15)
        begin_fill()
        circle(90, 120)
        seth(-52)
        circle(-90, 110)
        end_fill()
        
        # Large surprised eyes
        fillcolor('white')
        def large_eye():
            seth(-55)
            begin_fill()
            circle(28, 120)
            seth(-90)
            circle(-26, 165)
            end_fill()
        
        CoderHu(-100, 120)
        large_eye()
        CoderHu(40, 120)
        large_eye()
        
        # Black pupils
        fillcolor('black')
        CoderHu(-95, 108)
        circle(10)
        CoderHu(45, 108)
        circle(10)
        
        # Rest of body
        pencolor('red')
        fillcolor('orange')
        
        # Tilak
        def cir(r):
            begin_fill()
            circle(r)
            end_fill()
        
        CoderHu(0, 150)    
        cir(10)
        CoderHu(-2, 125)
        cir(8)
        CoderHu(-4, 105)
        cir(5)
        
        # Crown, ears, belly, legs, hands (simplified)
        CoderHu(-80, 200)
        seth(30)
        begin_fill()
        circle(-150, 60)
        seth(141)
        circle(120, 80)
        end_fill()
        
        time.sleep(0.4)
        
        # Back to normal
        clear()
        draw_ganesha()
        time.sleep(0.4)
    
    print("   ✓ Wide eyes animation complete!")

# ===== ANIMATION 3: HEAD NODDING =====
def head_nod_animation(nods=4):
    """Head nodding up and down"""
    print("🙏 Animation 3: Head Nodding...")
    global offset_y
    
    for i in range(nods):
        # Nod down
        clear()
        offset_y = -25
        draw_ganesha()
        time.sleep(0.25)
        
        # Back to center
        clear()
        offset_y = 0
        draw_ganesha()
        time.sleep(0.25)
    
    offset_y = 0
    print("   ✓ Head nodding complete!")

# ===== ANIMATION 4: TRUNK SWAYING =====
def trunk_sway_animation(sways=4):
    """Trunk moving side to side"""
    print("👃 Animation 4: Trunk Swaying...")
    global offset_x
    
    for i in range(sways):
        # Sway left
        clear()
        offset_x = -20
        draw_ganesha()
        time.sleep(0.3)
        
        # Center
        clear()
        offset_x = 0
        draw_ganesha()
        time.sleep(0.3)
        
        # Sway right
        clear()
        offset_x = 20
        draw_ganesha()
        time.sleep(0.3)
        
        # Center
        clear()
        offset_x = 0
        draw_ganesha()
        time.sleep(0.3)
    
    offset_x = 0
    print("   ✓ Trunk swaying complete!")

# ===== ANIMATION 5: HAND WAVING =====
def hand_wave_animation():
    """Hand waving animation"""
    print("🤚 Animation 5: Hand Waving...")
    
    for wave in range(3):
        # Draw Ganesha
        clear()
        draw_ganesha()
        
        # Draw waving hand (right)
        pencolor('red')
        fillcolor('orange')
        penup()
        goto(250, -40)
        pendown()
        seth(45)
        
        # Wave motion
        for j in range(3):
            penup()
            goto(250 + 15*math.sin(j*math.pi/3), -40 + 20*math.cos(j*math.pi/3))
            pendown()
            
            begin_fill()
            circle(20, 360)
            end_fill()
            
            time.sleep(0.15)
    
    clear()
    draw_ganesha()
    print("   ✓ Hand waving complete!")

# ===== ANIMATION 6: COLOR FLASHING =====
def color_flash_animation():
    """Color changing animation"""
    print("✨ Animation 6: Color Flashing...")
    
    colors = [
        ('red', 'orange'),
        ('yellow', 'gold'),
        ('white', 'yellow'),
        ('cyan', 'lightblue'),
        ('magenta', 'pink'),
        ('lime', 'lightgreen'),
        ('red', 'orange')
    ]
    
    for pen_col, fill_col in colors:
        clear()
        draw_ganesha(pen_col, fill_col)
        time.sleep(0.3)
    
    print("   ✓ Color flashing complete!")

# ===== ANIMATION 7: DANCING =====
def dancing_animation():
    """Full body dancing animation"""
    print("🕺 Animation 7: Dancing Movement...")
    global offset_x, offset_y
    
    dance_moves = [
        (-30, -20),  # Left-Down
        (0, 0),      # Center
        (30, -20),   # Right-Down
        (0, 0),      # Center
        (-20, 15),   # Left-Up
        (0, 0),      # Center
        (20, 15),    # Right-Up
        (0, 0),      # Center
    ]
    
    for move_x, move_y in dance_moves:
        clear()
        offset_x = move_x
        offset_y = move_y
        draw_ganesha()
        time.sleep(0.2)
    
    offset_x = 0
    offset_y = 0
    print("   ✓ Dancing complete!")

# ===== ANIMATION 8: SPINNING =====
def spinning_animation():
    """Ganesha spinning animation"""
    print("🌀 Animation 8: Spinning...")
    
    # Simple spinning effect by rotating drawing
    for angle in range(0, 360, 45):
        clear()
        
        # Simple rotation simulation - redraw with slight variations
        pencolor('red')
        fillcolor('orange')
        
        # Rotate turtle and draw
        seth(angle)
        draw_ganesha()
        time.sleep(0.2)
    
    seth(0)
    clear()
    draw_ganesha()
    print("   ✓ Spinning complete!")

# ===== ANIMATION 9: EYE ROLLING =====
def eye_rolling_animation():
    """Eyes rolling animation"""
    print("👁️ Animation 9: Eye Rolling...")
    
    # Draw body
    clear()
    pencolor('red')
    fillcolor('orange')
    
    # Main body parts
    CoderHu(-130, 150)
    seth(-120)
    begin_fill()
    circle(100, 90)
    circle(280, 10)
    circle(-120, 90)
    circle(-60, 150)
    circle(-30, 60)
    seth(-120)
    circle(30, 60)
    circle(55, 150)
    circle(120, 77)
    circle(-100, 115)
    end_fill()
    
    CoderHu(0, 50)
    seth(20)
    begin_fill()
    circle(-50, 80)
    circle(-200, 70)
    circle(-50, 60)
    seth(-20)
    circle(50, 70)
    circle(205, 70)
    circle(50, 85)
    end_fill()
    
    CoderHu(70, 10)
    seth(15)
    begin_fill()
    circle(90, 120)
    seth(-52)
    circle(-90, 110)
    end_fill()
    
    # Eyes rolling
    pencolor('red')
    fillcolor('white')
    
    eye_positions = [
        ((-100, 110), (-5, 0)),     # Center
        ((-100, 115), (5, 5)),      # Up-Right
        ((-100, 110), (10, 0)),     # Right
        ((-100, 105), (5, -5)),     # Down-Right
        ((-100, 100), (0, -10)),    # Down
        ((-100, 105), (-5, -5)),    # Down-Left
        ((-100, 110), (-10, 0)),    # Left
        ((-100, 115), (-5, 5)),     # Up-Left
        ((-100, 110), (0, 0)),      # Center
    ]
    
    for (left_pos, pupil_offset), (right_pos, pupil_offset) in zip(eye_positions, eye_positions):
        time.sleep(0.2)
    
    clear()
    draw_ganesha()
    print("   ✓ Eye rolling complete!")

# ===== ANIMATION 10: BREATHING =====
def breathing_animation():
    """Belly breathing animation (scale change)"""
    print("🫁 Animation 10: Breathing Motion...")
    global offset_y
    
    for i in range(4):
        # Inhale (expand)
        clear()
        offset_y = 5
        draw_ganesha()
        time.sleep(0.3)
        
        # Exhale (contract)
        clear()
        offset_y = -5
        draw_ganesha()
        time.sleep(0.3)
    
    offset_y = 0
    clear()
    draw_ganesha()
    print("   ✓ Breathing complete!")

# ===== ANIMATION 11: TILTING HEAD =====
def head_tilt_animation():
    """Head tilting left and right"""
    print("🤔 Animation 11: Head Tilting...")
    global offset_x
    
    for tilt in range(3):
        # Tilt right
        clear()
        offset_x = 30
        offset_y = -10
        draw_ganesha()
        time.sleep(0.3)
        
        # Center
        clear()
        offset_x = 0
        offset_y = 0
        draw_ganesha()
        time.sleep(0.3)
        
        # Tilt left
        clear()
        offset_x = -30
        offset_y = -10
        draw_ganesha()
        time.sleep(0.3)
        
        # Center
        clear()
        offset_x = 0
        offset_y = 0
        draw_ganesha()
        time.sleep(0.3)
    
    offset_x = 0
    offset_y = 0
    print("   ✓ Head tilting complete!")

# ===== ANIMATION 12: BLESSING GESTURE =====
def blessing_animation():
    """Hand blessing gesture"""
    print("🙏 Animation 12: Blessing Gesture...")
    
    for gesture in range(3):
        # Raise hand
        clear()
        offset_y = 20
        draw_ganesha()
        time.sleep(0.3)
        
        # Normal
        clear()
        offset_y = 0
        draw_ganesha()
        time.sleep(0.3)
    
    offset_y = 0
    print("   ✓ Blessing gesture complete!")

# ===== WELCOME MESSAGE =====
def show_welcome():
    """Display welcome message"""
    penup()
    goto(0, 350)
    pendown()
    pencolor('yellow')
    pensize(1)
    
    # Simple text
    write("🙏 JAI GANESHA 🙏", align="center", font=("Arial", 20, "bold"))
    
    penup()
    goto(0, -350)
    pendown()
    write("Vinayaka Chaturthi Celebrations", align="center", font=("Arial", 14, "normal"))

# ===== FINAL MESSAGE =====
def show_blessing():
    """Display blessing message"""
    penup()
    pencolor('gold')
    
    goto(0, 370)
    write("ॐ गं गणपतये नमः ॐ", align="center", font=("Arial", 16, "bold"))
    
    goto(0, -370)
    write("May Ganesha Remove All Obstacles & Bring Success!", align="center", font=("Arial", 12, "normal"))

# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("\n" + "="*60)
    print("🙏 GANESHA VINAYAKA CHATURTHI ANIMATION 🙏")
    print("="*60)
    print("\nStarting complete animation sequence...\n")
    
    # Initial drawing
    print("📍 Drawing Ganesha...")
    draw_ganesha()
    show_welcome()
    hideturtle()
    
    time.sleep(2)
    
    # Run all animations in sequence
    animations = [
        (blink_animation, {}),
        (wide_eyes_animation, {}),
        (head_nod_animation, {"nods": 3}),
        (trunk_sway_animation, {"sways": 3}),
        (hand_wave_animation, {}),
        (head_tilt_animation, {}),
        (breathing_animation, {}),
        (blessing_animation, {}),
        (color_flash_animation, {}),
        (dancing_animation, {}),
        (spinning_animation, {}),
        (eye_rolling_animation, {}),
    ]
    
    print("\n" + "="*60)
    print("ANIMATION SEQUENCE STARTING...")
    print("="*60 + "\n")
    
    for anim_func, kwargs in animations:
        anim_func(**kwargs)
        time.sleep(0.5)
    
    # Final scene
    print("\n" + "="*60)
    print("FINAL BLESSING...")
    print("="*60 + "\n")
    
    clear()
    pencolor('red')
    fillcolor('orange')
    draw_ganesha()
    show_blessing()
    hideturtle()
    
    print("✓ All animations complete!")
    print("\n🙏 Thank you for celebrating Ganesha Chaturthi! 🙏")
    print("\nPress any key to close...\n")
    
    done()