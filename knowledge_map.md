# Python 知识地图 (Knowledge Map) 🗺️

这份地图基于你的学习笔记 `star.py` 整理而成。
标记为 🃏 的部分是你接下来制作 **21点 (Blackjack)** 游戏时最核心的工具。

---

## 1. 核心装备 (Core Equipment) 🛡️
*这是构建游戏骨架的基础*

### 1.1 数据结构 (Data Structures)
| 概念 | 用途示例 | 21点相关性 |
| :--- | :--- | :--- |
| **List (列表)** | `deck = [card1, card2]`, `hand = []` | 🃏 **极高** (存储牌堆、手牌) |
| **Tuple (元组)** | `("Hearts", "K")`, `(10, 11)` | 🃏 **高** (定义不可变的牌属性、花色) |
| **Dictionary (字典)** | `{"K": 10, "Q": 10}` | 🃏 **中** (定义卡牌点数映射) |
| **Set (集合)** | `{"Roger", "Syd"}` | 低 (去重，扑克牌通常允许重复如多副牌) |

### 1.2 流程控制 (Control Flow)
| 概念 | 用途示例 | 21点相关性 |
| :--- | :--- | :--- |
| **While Loop** | `while True:` (游戏主循环) | 🃏 **极高** (保持游戏运行、等待玩家输入) |
| **For Loop** | `for card in hand:` | 🃏 **高** (计算手牌总分) |
| **If/Else** | `if score > 21:` (爆牌判断) | 🃏 **极高** (胜负判定、Ace算1还是11) |
| **Break/Continue**| `break` (跳出循环) | 🃏 **中** (玩家选择停牌 Stand) |

### 1.3 面向对象 (OOP)
*构建游戏世界的基石*

*   **Class (类)** 🃏
    *   `class Card:`: 定义一张牌的样子。
    *   `class Deck:`: 定义整副牌的行为（洗牌、发牌）。
    *   `class Hand:`: 定义玩家手里的牌（计算总分）。
*   **Methods (方法)**
    *   `__init__(self, ...)`: 初始化牌的花色、点数。
    *   `deal()`: 发牌动作。
*   **Inheritance (继承)**
    *   `class Player(Person):`: 玩家和庄家可能继承自同一个基类。

### 1.4 关键模块 (Modules)
*   **Random**: `import random`
    *   `random.shuffle(deck)`: **洗牌** (这是 `star.py` 没细讲但游戏必须的)。
    *   `random.choice(deck)`: 随机抽一张牌。

---

## 2. 进阶技能 (Advanced Skills) ⚡
*让你的代码更优雅、更健壮*

### 2.1 函数式编程 (Functional)
*   **Map**: `map(get_value, hand)` -> 快速提取手牌点数。
*   **Filter**: `filter(is_ace, hand)` -> 快速找出所有的 Ace。
*   **Lambda**: 简短的逻辑处理，如排序规则。
*   **List Comprehensions**: `[card.value for card in hand]` -> **推荐**，比 Map 更 Pythonic。

### 2.2 魔术方法 (Magic Methods)
让你的对象更智能：
*   `__str__` / `__repr__`: 当你 `print(card)` 时，显示 "♥️ K" 而不是 `<__main__.Card object...>`。
*   `__gt__`, `__lt__`: 让牌可以直接比较大小 (`card1 > card2`)。
*   `__add__`: 让两张牌可以直接相加 (`card1 + card2`)。

### 2.3 稳健性 (Robustness)
*   **Exceptions (异常处理)**: 防止玩家输入非数字导致崩溃 (`try...except ValueError`)。
*   **Decorators (装饰器)**: 可以用来记录游戏日志（如 `@log_game`）。
*   **Type Annotations**: `def calculate_score(hand: List[Card]) -> int:` (让代码更加清晰)。

---

## 3. 21点开发路线图 (Mini-Guide) 🚀

如果你不知道从哪开始，可以参考这个顺序：

1.  **定义 Card 类**: 有花色 (Suit) 和点数 (Rank)。
2.  **定义 Deck 类**: 生成 52 张 Card，实现 `shuffle()` (洗牌) 和 `deal()` (发牌)。
3.  **实现 Hand 类**: 能 `add_card()`，最重要的是 `calculate_value()` (处理 Ace 变 1 或 11 的逻辑)。
4.  **主循环 (Game Loop)**:
    *   发两张牌给 Player 和 Dealer。
    *   Player 回合：`input("Hit or Stand?")`。
    *   Dealer 回合：点数小于 17 必须拿牌。
    *   **判定胜负**: 比较分数，输出结果。

祝你编码愉快！
