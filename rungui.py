import tkinter as tk
from tkinter import ttk, messagebox
from lib.core import making_video
from lib.shortcore import final_video
from lib.video_texts import update_config_file, read_config_file

def save_config():
    if notebook.index(notebook.select()) == 0:
        update_config_file('config.txt', 'general_topic', general_topic_entry.get())
        update_config_file('config.txt', 'time', time_entry.get())
        update_config_file('config.txt', 'intro_video', intro_video_var.get())
        update_config_file('config.txt', 'pexels_api', pexels_entry.get())
        update_config_file('config.txt', 'language', language_combobox.get())
        update_config_file('config.txt', 'multi_speaker', multi_speaker_var.get())
        messagebox.showinfo("Run", "program run successfully!")
        root.withdraw()  
        making_video(topic_entry.get())
    elif notebook.index(notebook.select()) == 1:
        update_config_file('config.txt', 'multi_speaker', multi_speaker_var2.get())
        update_config_file('config.txt', 'pexels_api', pexels_entry2.get())
        messagebox.showinfo("Run", "program run successfully!")
        root.withdraw()  
        final_video(topic_entry2.get(), time_entry2.get(), language_combobox2.get(), multi_speaker_var.get())
    elif notebook.index(notebook.select()) == 2:
        update_config_file('config.txt', 'title', title_entry.get())
        update_config_file('config.txt', 'video-content', video_content_entry.get())
        update_config_file('config.txt', 'time', time_entry3.get())
        update_config_file('config.txt', 'intro_video', intro_video_var3.get())
        update_config_file('config.txt', 'pexels_api', pexels_entry3.get())
        update_config_file('config.txt', 'language', language_combobox3.get())
        update_config_file('config.txt', 'multi_speaker', multi_speaker_var3.get())
        messagebox.showinfo("Run", "program run successfully!")
        root.withdraw()

root = tk.Tk()
root.title("Configurator")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)

notebook.add(frame1, text='long video')
notebook.add(frame2, text='short video')
notebook.add(frame3, text='custom video')

def add_label_with_description(frame, row, text, description):
    ttk.Label(frame, text=f"{text}: {description}", wraplength=400, justify='left').grid(row=row, column=0, columnspan=2, padx=5, pady=5, sticky='w')

# Frame 1 Widgets
add_label_with_description(frame1, 0, "topic", "Enter video topic. Example: survival video game")
add_label_with_description(frame1, 1, "general topic", "general topic you want to make a video about.Example: video game, food, city, person and...")
add_label_with_description(frame1, 2, "Time", "video time in minute")
add_label_with_description(frame1, 3, "Intro Video", "do you want intro with video instead photo?")
add_label_with_description(frame1, 4, "Pexels API", "if yes , get API from www.pexels.com")
add_label_with_description(frame1, 5, "Language", "video language")
add_label_with_description(frame1, 6, "multi speaker", "Use multiple speakers in video")

topic_entry = tk.Entry(frame1)
topic_entry.grid(row=0, column=2, padx=5, pady=5)
general_topic_entry = tk.Entry(frame1)
general_topic_entry.grid(row=1, column=2, padx=5, pady=5)
time_entry = tk.Entry(frame1)
time_entry.grid(row=2, column=2, padx=5, pady=5)
intro_video_var = tk.StringVar(value="yes")
intro_video_checkbox = ttk.Checkbutton(frame1, variable=intro_video_var, onvalue="yes", offvalue="no")
intro_video_checkbox.grid(row=3, column=2, padx=5, pady=5)
pexels_entry = tk.Entry(frame1)
pexels_entry.grid(row=4, column=2, padx=5, pady=5)
language_combobox = ttk.Combobox(frame1, values=["persian", "english", "arabic", "vietnamese", "zulu", "afrikaans", "amharic", "azerbaijani", "bulgarian", "bengali", "bosnian", "catalan", "czech", "welsh", "danish", "german", "greek", "spanish", "estonian", "filipino", "finnish", "french", "irish", "galician", "gujarati", "hebrew", "hindi", "croatian", "hungarian", "indonesian", "icelandic", "italian", "japanese", "javanese", "georgian", "kazakh", "khmer", "kannada", "korean", "lao", "lithuanian", "latvian", "macedonian", "malayalam", "mongolian", "marathi", "malay", "maltese", "burmese", "norwegian", "nepali", "dutch", "polish", "pashto", "portuguese", "romanian", "russian", "sinhala", "slovak", "slovenian", "somali", "albanian", "serbian", "sundanese", "swedish", "swahili", "tamil", "telugu", "thai", "turkish", "ukrainian", "urdu", "uzbek"])
language_combobox.grid(row=5, column=2, padx=5, pady=5)
multi_speaker_var = tk.StringVar(value="yes")
multi_speaker_checkbox = ttk.Checkbutton(frame1, variable=multi_speaker_var, onvalue="yes", offvalue="no")
multi_speaker_checkbox.grid(row=6, column=2, padx=5, pady=5)

# Frame 2 Widgets
add_label_with_description(frame2, 0, "topic", "Enter video topic. Example: survival video game")
add_label_with_description(frame2, 1, "Time", "video time in second")
add_label_with_description(frame2, 2, "Language", "video language")
add_label_with_description(frame2, 3, "multi speaker", "Use multiple speakers in video")
add_label_with_description(frame2, 4, "Pexels API", "if yes , get API from www.pexels.com")

topic_entry2 = tk.Entry(frame2)
topic_entry2.grid(row=0, column=2, padx=5, pady=5)
time_entry2 = tk.Entry(frame2)
time_entry2.grid(row=1, column=2, padx=5, pady=5)
language_combobox2 = ttk.Combobox(frame2, values=["persian", "english", "arabic", "vietnamese", "zulu", "afrikaans", "amharic", "azerbaijani", "bulgarian", "bengali", "bosnian", "catalan", "czech", "welsh", "danish", "german", "greek", "spanish", "estonian", "filipino", "finnish", "french", "irish", "galician", "gujarati", "hebrew", "hindi", "croatian", "hungarian", "indonesian", "icelandic", "italian", "japanese", "javanese", "georgian", "kazakh", "khmer", "kannada", "korean", "lao", "lithuanian", "latvian", "macedonian", "malayalam", "mongolian", "marathi", "malay", "maltese", "burmese", "norwegian", "nepali", "dutch", "polish", "pashto", "portuguese", "romanian", "russian", "sinhala", "slovak", "slovenian", "somali", "albanian", "serbian", "sundanese", "swedish", "swahili", "tamil", "telugu", "thai", "turkish", "ukrainian", "urdu", "uzbek"])
language_combobox2.grid(row=2, column=2, padx=5, pady=5)
multi_speaker_var2 = tk.StringVar(value="yes")
multi_speaker_checkbox2 = ttk.Checkbutton(frame2, variable=multi_speaker_var2, onvalue="yes", offvalue="no")
multi_speaker_checkbox2.grid(row=3, column=2, padx=5, pady=5)
pexels_entry2 = tk.Entry(frame2)
pexels_entry2.grid(row=4, column=2, padx=5, pady=5)

# Frame 3 Widgets
add_label_with_description(frame3, 0, "title", "Video Title")
add_label_with_description(frame3, 1, "video-content", "video content")
add_label_with_description(frame3, 2, "Time", "video time in minute")
add_label_with_description(frame3, 3, "Intro_video", "video intro")
add_label_with_description(frame3, 4, "Pexels_api", "api")
add_label_with_description(frame3, 5, "Language", "english")
add_label_with_description(frame3, 6, "Multi_speaker", "no")

title_entry = tk.Entry(frame3)
title_entry.grid(row=0, column=2, padx=5, pady=5)
video_content_entry = tk.Entry(frame3)
video_content_entry.grid(row=1, column=2, padx=5, pady=5)
time_entry3 = tk.Entry(frame3)
time_entry3.grid(row=2, column=2, padx=5, pady=5)
intro_video_var3 = tk.StringVar(value="yes")
intro_video_checkbox3 = ttk.Checkbutton(frame3, variable=intro_video_var3, onvalue="yes", offvalue="no")
intro_video_checkbox3.grid(row=3, column=2, padx=5, pady=5)
pexels_entry3 = tk.Entry(frame3)
pexels_entry3.grid(row=4, column=2, padx=5, pady=5)
language_combobox3 = ttk.Combobox(frame3, values=["persian", "english", "arabic", "vietnamese", "zulu", "afrikaans", "amharic", "azerbaijani", "bulgarian", "bengali", "bosnian", "catalan", "czech", "welsh", "danish", "german", "greek", "spanish", "estonian", "filipino", "finnish", "french", "irish", "galician", "gujarati", "hebrew", "hindi", "croatian", "hungarian", "indonesian", "icelandic", "italian", "japanese", "javanese", "georgian", "kazakh", "khmer", "kannada", "korean", "lao", "lithuanian", "latvian", "macedonian", "malayalam", "mongolian", "marathi", "malay", "maltese", "burmese", "norwegian", "nepali", "dutch", "polish", "pashto", "portuguese", "romanian", "russian", "sinhala", "slovak", "slovenian", "somali", "albanian", "serbian", "sundanese", "swedish", "swahili", "tamil", "telugu", "thai", "turkish", "ukrainian", "urdu", "uzbek"])
language_combobox3.grid(row=5, column=2, padx=5, pady=5)
multi_speaker_var3 = tk.StringVar(value="no")
multi_speaker_checkbox3 = ttk.Checkbutton(frame3, variable=multi_speaker_var3, onvalue="yes", offvalue="no")
multi_speaker_checkbox3.grid(row=6, column=2, padx=5, pady=5)

# Frame 1 Defaults
topic_entry.insert(0, "survival video game")
general_topic_entry.insert(0, read_config_file()['general_topic'])
time_entry.insert(0, read_config_file()['time'])
intro_video_var.set(read_config_file()['intro_video'])
pexels_entry.insert(0, read_config_file()['pexels_api'])
language_combobox.set(read_config_file()['language'])
multi_speaker_var.set(read_config_file()['multi_speaker'])

# Frame 2 Defaults
topic_entry2.insert(0, "survival video game")
time_entry2.insert(0, "30")
language_combobox2.set("english")
multi_speaker_var2.set(read_config_file()['multi_speaker'])
pexels_entry2.insert(0, read_config_file()['pexels_api'])

# Frame 3 Defaults
title_entry.insert(0, "Video Title")
video_content_entry.insert(0, "Content")
time_entry3.insert(0, "10")
intro_video_var3.set("yes")
pexels_entry3.insert(0, "API")
language_combobox3.set("english")
multi_speaker_var3.set("no")

save_button = tk.Button(root, text="run", command=save_config)
save_button.pack(pady=10)

root.mainloop()
