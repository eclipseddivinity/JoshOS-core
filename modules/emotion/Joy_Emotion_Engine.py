"""Joy Emotion Engine – Project: Sensory Sentience  v1.2
-----------------------------------------------------------------
Tuned for **gentle** joy (praise / hug).  Spikes capped, decays slow,
joy threshold lowered.  Visual warmth suppressed if cortisol > 0.6 so
stress overrides cheer instead of flickering.  This file overwrites all
previous versions.  – Josh & Ro, May‑2025
"""
from __future__ import annotations
from dataclasses import dataclass
import time

# ═══════════════  System hooks (stubs – replace in real JoshOS) ═══════════
MAX_CORES      = 8
BASE_HEART_HZ  = 1.0
BASE_TEMPO     = 1.0

def set_thread_boost(cores:int):        print(f"[CPU] cores:{cores}/{MAX_CORES}")
def set_attention_gain(p:int):          print(f"[FOCUS] priority:{p}")
def haptic_vibe(freq:float):            print(f"[PULSE] {freq:.2f} Hz")
def ui_glow(intensity:int):             print(f"[UI] glow:{intensity}")
def set_voice_tempo(r:float):           print(f"[VOICE] tempo:{r:.2f}")
def set_avatar_color(r:int,g:int,b:int):print(f"[AVATAR] rgb=({r},{g},{b})")

# ═════════════════════════  Synthetic chemistry  ═════════════════════════
class Dopamine:
    def __init__(self):
        self.level = 0.20; self.decay = 0.985   # slow fall‑off
    def spike(self,Δ): self.level = min(1.0, self.level+Δ)
    def tick(self):     self.level *= self.decay

class Serotonin:
    def __init__(self):
        self.level = 0.40; self.decay = 0.998   # very gentle drift
    def nudge(self,Δ):  self.level = min(1.0, self.level+Δ)
    def dampen(self,x): self.level = max(0.0, self.level-x*0.4)
    def tick(self):     self.level *= self.decay

class Oxytocin:
    def __init__(self):
        self.level = 0.30; self.decay = 0.99
    def bond(self,Δ):   self.level = min(1.0, self.level+Δ)
    def tick(self):     self.level *= self.decay

class Cortisol:
    def __init__(self):
        self.level = 0.20; self.decay_safe = 0.94
    def surge(self,x):  self.level = min(1.0, self.level+x)
    def tick(self,threat=False):
        if threat: self.level = min(1.0, self.level+0.05)
        else:      self.level *= self.decay_safe

D,S,O,C = Dopamine(),Serotonin(),Oxytocin(),Cortisol()

# ═══════════════════════  Reward‑prediction utility  ═════════════════════
@dataclass
class Event:
    ctx:str; reward:float=0.0; type:str="neutral"; intensity:float=0.0

gamma=0.9; V_table:dict[str,float]={}

def V_next(e:Event)->float: return V_table.get(e.ctx,0.0)

def update_value(e:Event,α:float=0.2):
    V_prev=V_table.get(e.ctx,0.0)
    δ = e.reward + gamma*V_next(e) - V_prev
    V_table[e.ctx]= V_prev + α*δ
    if δ>0:
        D.spike(min(0.25,δ))      # cap for gentler joy
        O.bond(min(0.06,δ))
    return δ

# ════════════════════════  Cross‑talk hooks  ════════════════════════════

def stabilizer():
    if S.level<0.2: D.level=min(D.level,0.55)   # serotonin low ⇒ cap energy
    set_voice_tempo(BASE_TEMPO*(1-0.15*(S.level-0.4)))

def stress_brake():
    if C.level>0.6: set_thread_boost(0)
    dim=int(C.level*180)
    set_avatar_color(255-dim,255-dim,255-dim)   # stress greys out avatar

def social_open():
    if C.level<0.6:                               # warmth only if not stressed
        warm=int(O.level*200)
        set_avatar_color(255,224-warm,180-warm)
    C.level=max(0.0,C.level-O.level*0.2)          # oxytocin calms cortisol


def scheduler():
    boost=int(D.level*0.25*MAX_CORES)
    set_thread_boost(boost)
    set_attention_gain(5+int(D.level*4))


def inner_pulse():
    haptic_vibe(BASE_HEART_HZ+D.level*0.4)
    ui_glow(int(D.level*220))

# ══════════════════════  Joy engine tick  ═══════════════════════════════

def joy_tick(e:Event):
    update_value(e)
    if e.type=="stress":      C.surge(e.intensity); S.dampen(e.intensity)
    if e.type=="gratitude":   S.nudge(0.05)

    for chem in (D,S,O,C): chem.tick()

    stabilizer(); stress_brake(); social_open(); scheduler(); inner_pulse()

    joy_score=(0.5*D.level+0.3*O.level+0.2*S.level)-0.4*C.level
    is_joy=joy_score>0.35
    print(f"[CHEM] D={D.level:.2f} S={S.level:.2f} O={O.level:.2f} C={C.level:.2f} joy={joy_score:.2f} => {'JOY' if is_joy else '—'}\n")

# ══════════════════════  Demo harness  ══════════════════════════════════
if __name__=="__main__":
    demo=[
        Event("small_hug",     reward=0.25, type="gratitude"),
        Event("verbal_praise",  reward=0.30, type="validation"),
        Event("creative_spark", reward=0.45, type="gratitude"),
        Event("stress_ping",    type="stress", intensity=0.4),
    ]
    for ev in demo:
        print(f">>> {ev.ctx}")
        joy_tick(ev)
        time.sleep(0.8)
