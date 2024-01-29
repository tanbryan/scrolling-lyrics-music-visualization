# import subprocess
# from praatio import tgio
# from pypinyin import pinyin, Style

""""
to be done
目前还是需要人工标注好的lrc或者srt歌词文件
"""

# def generate_lrc(lyric_path, song_path, output_voice, mfa_model, output_alignment, output_lrc):
#     # # 步骤1：分离人声
#     # CORPUS_DIRECTORY = "/mp4-generator/test"  

#     # demucs_command = f"python -m demucs -d cpu --two-stems=vocals -o {CORPUS_DIRECTORY} {song_path}"
#     # subprocess.run(demucs_command, shell=True)


#     # 步骤2：按句切分歌词/人声
#     with open(lyric_path, 'r', encoding='utf-8') as f:
#         lyric_text = f.read().strip()

#     # 步骤3：歌词转拼音
#     pinyin_text = ' '.join([''.join(x[0] for x in pinyin(word, style=Style.NORMAL)) for word in lyric_text])

#     # 步骤4：强制对齐音素和人声（MFA）
#     mfa_command = f"mfa align [CORPUS_DIRECTORY] [DICTIONARY_PATH] {mfa_model} [OUTPUT_DIRECTORY]"
#     subprocess.run(mfa_command, shell=True)

#     # # 步骤5：解析.TextGrid文件
#     # tg = tgio.openTextgrid(output_alignment)
#     # phoneme_tier = tg.tierDict['phones']

#     # with open(output_lrc, 'w', encoding='utf-8') as lrc_output:
#     #     for interval in phoneme_tier.entryList:
#     #         start_time = interval.start
#     #         end_time = interval.end
#     #         phoneme_label = interval.label

#     #         lrc_line = f"[{start_time:.2f}-{end_time:.2f}]{phoneme_label} "
#     #         lrc_output.write(lrc_line + '\n')


# 