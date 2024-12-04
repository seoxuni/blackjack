import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class BlackjackTable:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("블랙잭 게임")
        
        # 카드 이미지 로드
        self.card_images = {}
        self.load_card_images()
        
        self.root.geometry("800x600")

        self.root.resizable(False, False)
        
        # 메인 프레임
        self.main_frame = tk.Frame(self.root, bg='#2d8653')
        self.main_frame.pack(fill='both', expand=True)
        
        # 딜러 영역
        self.dealer_frame = tk.Frame(self.main_frame, bg='#2d8653')
        self.dealer_frame.place(relx=0, rely=0, relwidth=1, relheight=0.5)
        
        self.dealer_label = tk.Label(self.dealer_frame, text="딜러", 
                                   font=('Pretendard Variable', 14), bg='#2d8653', fg='white')
        self.dealer_label.pack(pady=5)
        
        self.dealer_cards_frame = tk.Frame(self.dealer_frame, bg='#2d8653')
        self.dealer_cards_frame.pack(fill='both', expand=True)

        self.dealer_cards_holder = tk.Frame(self.dealer_cards_frame, bg='#2d8653', 
                                          width=700, height=200, bd=2, relief='solid')
        self.dealer_cards_holder.pack(pady=(20, 35), anchor='center')
        self.dealer_cards_holder.pack_propagate(False) 
        
        # 구분선
        self.separator = tk.Frame(self.main_frame, bg='#FFFFFF', height=4)
        self.separator.place(relx=0, rely=0.5, relwidth=1)
        
        # 플레이어 영역
        self.player_frame = tk.Frame(self.main_frame, bg='#2d8653')
        self.player_frame.place(relx=0, rely=0.51, relwidth=1, relheight=0.49)
        
        self.player_cards_frame = tk.Frame(self.player_frame, bg='#2d8653')
        self.player_cards_frame.pack(fill='both', expand=True)
        
        self.player_cards_holder = tk.Frame(self.player_cards_frame, bg='#2d8653', 
                                          width=700, height=200, bd=2, relief='solid')
        self.player_cards_holder.pack(pady=(35, 20), anchor='center')
        self.player_cards_holder.pack_propagate(False) 
        
        self.player_label = tk.Label(self.player_frame, text="플레이어", 
                                   font=('Pretendard Variable', 14), bg='#2d8653', fg='white')
        self.player_label.pack(pady=5)

    def load_card_images(self):
        """카드 이미지 로드"""
        cards_dir = "cards"  # 카드 이미지가 있는 디렉토리
        for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
            for value in range(1, 14):
                image_path = os.path.join(cards_dir, "2D.png")
                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    # 카드 크기 조정
                    image = image.resize((100, 145), Image.Resampling.LANCZOS)
                    photo_image = ImageTk.PhotoImage(image)
                    self.card_images[f"{suit}_{value}"] = photo_image

    def add_card_to_dealer(self, card_name):
        """딜러 영역에 카드 추가"""
        if card_name in self.card_images:
            card_label = tk.Label(self.dealer_cards_holder, image=self.card_images[card_name])
            card_label.pack(side='left', padx=5)

    def add_card_to_player(self, card_name):
        """플레이어 영역에 카드 추가"""
        if card_name in self.card_images:
            card_label = tk.Label(self.player_cards_holder, image=self.card_images[card_name])
            card_label.pack(side='left', padx=5)

    def test_add_cards(self):
        """테스트용 카드 추가"""
        self.add_card_to_dealer("hearts_1")
        self.add_card_to_dealer("spades_12")
        self.add_card_to_player("diamonds_10")
        self.add_card_to_player("clubs_5")

    def run(self):
        # 테스트용 카드 추가
        self.test_add_cards()
        self.root.mainloop()

if __name__ == "__main__":
    game = BlackjackTable()
    game.run()
