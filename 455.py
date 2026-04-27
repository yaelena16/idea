import tkinter as tk
import random
#список творческих идей
art_ideas = [
    "Нарисуйте фантастическое животное, которое живёт в облаках.",
    "Изобразите чашку кофе, в которой отражается космос.",
    "Придумайте и нарисуйте новый вид транспорта для путешествий во времени.",
    "Создайте портрет вашего настроения в виде абстрактной композиции.",
    "Нарисуйте, как выглядит музыка, когда её можно увидеть."
]

# Ссылка на плейлист с вдохновляющей музыкой (условная)
inspiration_url = "https://example.com/inspiration_playlist"

#Главное окно
root = tk.Tk()
root.title("Генератор идей для рисования")
root.geometry("600x250")
root.configure(bg="#f0f0f0")

#Создаём метку для отображения идеи
idea_label = tk.Label(
    root,
    text="Нажмите кнопку чтобы получить идею для рисования",
    wraplength=550,
    justify="center",
    font=("Georgia", 12, "bold"),
    bg="#f0f0f0",
    fg="#333333",
)
idea_label.pack(pady=30)

#Функция для показа случайной идеи
def show_idea():
    idea=random.choice(art_ideas)
    idea_label.config(text=idea)

#Кнопка для регенерации идей
generate_btn = tk.Button(
    root,
    text="Новая идея",
    command=show_idea,
    font=("Georgia", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    cursor="hand2"
)
generate_btn.pack(pady=10)

root.mainloop()