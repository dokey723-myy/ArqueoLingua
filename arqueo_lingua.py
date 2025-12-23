import re
import sys

# 尝试导入颜色库，如果没有安装，则定义空类以防报错
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class Fore: RED = GREEN = BLUE = CYAN = YELLOW = RESET = ""
    class Style: BRIGHT = ""

class ArqueoLingua:
    def __init__(self):
        print(f"{Fore.CYAN}{Style.BRIGHT}=== ArqueoLingua: 考古学西语解码器 v1.0 ==={Fore.RESET}")
        print("正在加载词源逻辑库...\n")
        
        # 1. 考古核心词库 (你可以随时在这里添加新词)
        self.archaeo_dict = {
            # 物质遗存
            "hueso": "骨头", "piedra": "石头", "fuego": "火",
            "ofrenda": "祭品", "entierro": "墓葬", "sitio": "遗址", "tumba": "坟墓",
            "concha": "贝壳", "cerámica": "陶器", "muro": "墙",
            
            # 建筑与空间
            "pirámide": "金字塔", "plaza": "广场", "hundida": "下沉的",
            "plataforma": "平台", "templo": "神庙", "canal": "水渠",
            "norte": "北", "sur": "南", "este": "东", "oeste": "西",
            
            # 抽象概念 & 萨满
            "poder": "权力", "sagrado": "神圣的", "chamanismo": "萨满教",
            "cosmovisión": "宇宙观", "dualidad": "二元性", "ritual": "仪式",
            "antiguo": "古老的", "desarrollo": "发展", "origen": "起源",
            
            # 卡拉尔特色 (讲座专用)
            "caral": "卡拉尔(文明)", "shicras": "希克拉(石袋)", "quipu": "奇普(结绳)",
            "flauta": "笛子", "spondylus": "海菊蛤", "supe": "苏佩(谷地)"
        }

    def analyze_sentence(self, sentence):
        # 预处理：移除多余符号
        clean_sentence = re.sub(r'[^\w\s]', '', sentence)
        words = clean_sentence.split()
        
        print(f"{Fore.YELLOW}>>> 原文句子: {sentence}{Fore.RESET}")
        print("-" * 60)
        print(f"{'单词 (西)':<18} | {'类型':<8} | {'解码含义'}")
        print("-" * 60)

        for word in words:
            original_word = word
            lower_word = word.lower()
            tag = ""
            note = ""
            color = Fore.WHITE

            # --- 逻辑层 1: 考古词库匹配 (Archaeo Radar) ---
            if lower_word in self.archaeo_dict:
                tag = "⛏️ 术语"
                note = self.archaeo_dict[lower_word]
                color = Fore.RED

            # --- 逻辑层 2: 动词时态黑客 (Verb Hunter) ---
            # 识别过去时 (-ó, -ron) 和不定式 (-ar, -er, -ir)
            elif lower_word.endswith("ó") or lower_word.endswith("ron"):
                tag = "⚡ 动作"
                note = "核心动词 (过去时: 做了...)"
                color = Fore.BLUE
            elif lower_word.endswith("ar") or lower_word.endswith("er") or lower_word.endswith("ir"):
                tag = "⚡ 动作"
                note = "动词原形"
                color = Fore.BLUE

            # --- 逻辑层 3: 同源词识别 (Cognate Scanner) ---
            elif lower_word.endswith("ción"):
                tag = "🇬🇧 同源"
                note = f"-> {lower_word[:-4]}tion"
                color = Fore.GREEN
            elif lower_word.endswith("dad"):
                tag = "🇬🇧 同源"
                note = f"-> {lower_word[:-3]}ty"
                color = Fore.GREEN
            elif lower_word.endswith("ía"):
                tag = "🇬🇧 同源"
                note = f"-> {lower_word[:-2]}y"
                color = Fore.GREEN
            elif lower_word.endswith("ismo"):
                tag = "🇬🇧 同源"
                note = f"-> {lower_word[:-4]}ism"
                color = Fore.GREEN
            elif lower_word.endswith("al"):
                tag = "🇬🇧 同源"
                note = "-> (可能与英语拼写相同)"
                color = Fore.GREEN

            # --- 逻辑层 4: 结构词 (Structure) ---
            elif lower_word in ["de", "la", "el", "los", "las", "un", "una"]:
                tag = "⚪ 冠/介"
                note = "的 / 一个 / 那个"
                color = Fore.LIGHTBLACK_EX
            elif lower_word in ["y", "o", "pero", "para", "con", "en"]:
                tag = "🔗 连接"
                trans = {"y":"和", "o":"或", "pero":"但是", "para":"为了", "con":"用/伴随", "en":"在"}
                note = trans.get(lower_word, "连接词")
                color = Fore.CYAN

            # 输出结果
            if note:
                print(f"{color}{original_word:<18} | {tag:<8} | {note}{Fore.RESET}")
            else:
                # 没识别出来的词，留白，不产生噪音
                pass
        print("-" * 60 + "\n")

if __name__ == "__main__":
    app = ArqueoLingua()
    
    # 默认测试句 (卡拉尔讲座相关)
    default_text = "La sociedad de Caral usó el fuego para conectar con la energía del cielo."
    app.analyze_sentence(default_text)

    # 交互模式
    while True:
        user_input = input("请输入一句西语 (输入 'q' 退出): ")
        if user_input.lower() == 'q':
            break
        app.analyze_sentence(user_input)
