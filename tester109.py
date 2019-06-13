# VERSION OCTOBER 7, 2018

from hashlib import sha256
from time import time

import labs109
import itertools
import random
import re
import sys

# Make sure that the source code file does not contain even one
# print or input statement, except after the part that is run when
# the module is run as a standalone application.

def has_banned_stuff(filename, banned = ['input']):
    file = open(filename, encoding='utf-8')
    for line in file:
        if line.strip().startswith("if __name__ =="):
            break # anything goes after that
        for word in banned:
            if line.find(word) > -1:
                return True
    file.close()
    return False

# Runs the function f for all testcases, calculating SHA256 checksum
# of the results. If the checksum matches the expected, return the
# running time, otherwise return -1. If expected == None, print out
# the computed checksum instead.

def test_one_function(f, testcases, expected = None):
    print(f.__name__ + ": ", end="", flush = True)
    chk = sha256()
    starttime = time()
    crashed = False
    for elem in testcases:
        try:
            result = f(*elem)
        except: # catch any exception thrown by the function to be tested
            crashed = True
            break
        # If the result is a dictionary, canonize its representation first.
        if type(result) == type({}):
            result = [(key, result[key]) for key in result]
            result.sort(key = lambda x: x[0])
        # Use the result to update the checksum.
        chk.update(str(result).encode('utf-8'))
    totaltime = time() - starttime
    digest = chk.hexdigest()
    if not crashed and not expected:
        print(digest[:50])
        return totaltime
    elif not crashed and digest[:len(expected)] == expected:
        print("Success in %.3f seconds." % totaltime)
        return totaltime
    elif crashed:
        print(f"CRASH: {sys.exc_info()[0]}")
    else:
        print("Failed the test with checksum mismatch.".upper())
        return -1

# Runs the tests for all functions in the suite, returning the
# count of how many of those were implemented and passed the test.

def test_all_functions(module, suite, modulename = None):
    if modulename:
        if has_banned_stuff(modulename):
            print("The file %s contains banned stuff in functions. Exiting." %
                  modulename)
            return 0
    count = 0
    total = 0
    for (fname, testcases, expected) in suite:
        try:
            f = module.__dict__[fname]
        except KeyError:
            #print("Function [%s] not implemented, skipping..." % fname)
            continue
        total += 1
        result = test_one_function(f, testcases, expected)
        if result >= 0:
            count += 1
    print("%d out of %d implemented functions (of %d total) pass the tester."
          % (count, total, len(suite)))
    return count

def ryerson_letter_grade_generator():
    for i in range(0, 150):
        yield (i,)
        
def is_ascending_generator(n):
    for i in range(n):
        for seq in itertools.permutations(range(n)):
            yield [seq]

def double_until_all_digits_generator():
    for i in range(3000):
        yield (i,)

def group_equal_generator(seed):
    random.seed(seed)
    for i in range(1000):
        items = []
        ilen = random.randint(1, 20)
        for j in range(ilen):
            burst = random.randint(1, 10)
            it = random.randint(0, 1000)
            for k in range(burst):
                items.append(it)
        yield (items,)

def longest_palindrome_generator(seed):
    random.seed(seed)
    for i in range(1000):
        m = random.randint(5, 50)
        text = ""
        for j in range(m):
            text += random.choice(["a","b","c","d"])
        yield (text, )

def caps_lock_stuck_generator():
    wap = open("warandpeace.txt", encoding='utf-8')
    text = list(wap)
    wap.close()
    for line in text:
        yield (line,)
        
def values_to_keys_generator(seed):
    random.seed(seed)
    for i in range(1000):
        used_values = set()
        used_keys = set()
        dic = {}
        size = random.randint(5, 100)
        while len(dic) < size:
            key = random.randint(-1000, 1000)
            value = random.randint(-1000, 1000)
            if key in used_keys or value in used_values:
                continue
            used_keys.add(key)
            used_values.add(value)
            dic[key] = value
        yield (dic,)
        
def paragraph_lengths_generator():
    wap = open("warandpeace.txt", encoding='utf-8')
    text = list(wap)
    wap.close()
    yield (text,)
    
def reverse_ascending_sublists_generator(seed):
    random.seed(seed)
    for i in range(1000):
        curr = []
        n = random.randint(0, 20)
        for j in range(n):
            curr.append(random.randint(0, 10000))
        yield (curr, )
    
def give_change_generator(seed):
    random.seed(seed)
    for i in range(100000):
        coins = [1]
        curr = 1
        c = random.randint(2, 5)
        for j in range(c):
            curr = curr + random.randint(3, 30)
            coins.append(curr)
        coins.reverse()
        yield (random.randint(1, 500), coins)
    

suits = ['clubs', 'diamonds', 'hearts', 'spades']
ranks = {'deuce' : 2, 'trey' : 3 , 'four' : 4, 'five' : 5,
         'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9,
         'ten' : 10, 'jack' : 11, 'queen' : 12, 'king' : 13,
         'ace' : 14 }

deck = [ (rank, suit) for suit in suits for rank in ranks.keys() ]

def hand_is_badugi_generator(seed):
    random.seed(seed)
    for i in range(100000):
        yield (random.sample(deck, 4),)

def bridge_hand_shape_generator(seed):
    random.seed(seed)
    for i in range(20000):
        yield (random.sample(deck, 13),)

def winning_card_generator(seed):
    random.seed(seed)
    for i in range(10000):
        hand = random.sample(deck, 4)
        for trump in ["spades", "hearts", "diamonds", "clubs", None]:            
            yield (hand, trump)

def hand_shape_distribution_generator(seed):
    random.seed(seed)
    hands = [random.sample(deck, 13) for i in range(10000)]
    yield [hands]

def milton_work_point_count_generator(seed):
    random.seed(seed)
    strains = suits + ['notrump']
    for i in range(50000):
        st = random.choice(strains)
        hand = random.sample(deck, 13)
        yield (hand, st)

def limited_alphabet(words, chars):
    pat = re.compile('^[' + chars + ']+$')
    result = []
    for word in words:
        if pat.match(word):
            result.append(word)
    return result

def sort_by_typing_handedness_generator():
    f = open('words.txt', 'r', encoding='utf-8')
    words = [x.strip() for x in f if x.islower()]
    f.close()
    words = limited_alphabet(words, "abcdefghijklmnopqrstuvwxyz")
    yield [words]

def letter_pair_freqs_generator():
    f = open('words.txt', 'r', encoding='utf-8')
    words = [x.strip() for x in f if x.islower()]
    f.close()
    words = limited_alphabet(words, "abcdefghijklmnopqrstuvwxyz")
    yield [words]

def possible_words_generator(seed):
    f = open('words.txt', 'r', encoding='utf-8')
    words = [x.strip() for x in f if x.islower()]
    f.close()
    random.seed(seed)
    for i in range(100):
        patword = random.choice(words)
        pat = ""
        for ch in patword:
            if random.randint(0, 99) < 60:
                pat += '*'
            else:
                pat += ch
        yield (words, pat)
                
def word_salad_generator(seed):
    f = open('words.txt', 'r', encoding='utf-8')
    words = [x.strip() for x in f if x.islower()]
    f.close()
    random.seed(seed)
    for i in range(100):
        leng = random.randint(3, 10)
        num = random.randint(3, 6)
        ingredients = []
        while len(ingredients) < num:
            word = random.choice(words)
            if len(word) == leng:
                ingredients.append(word)
        yield (words, ingredients)    

def postfix_evaluate_generator(seed):
    for i in range(1000):
        exp = []
        count = 0
        while len(exp) < 5 or count != 1:
            if count > 1 and (count > 10 or random.randint(0, 99) < 50):
                exp.append(random.choice(['+', '-', '*', '/']))
                count -= 1
            else:
                exp.append(random.randint(1, 10))
                count += 1
        yield (exp, )

def create_list(d):
    if d < 1:
        return random.randint(1, 100)
    else:
        n = random.randint(0, 10 - d)
        return [create_list(d - random.randint(1, 3)) for i in range(n)]

def reverse_reversed_generator(seed):
    random.seed(seed)
    for i in range(1000):
        items = create_list(1 + (i % 8))
        yield (items, )

def brick_wall_generator(seed):
    random.seed(seed)
    for i in range(1000):
        ht = random.randint(1, 100)
        n = random.randint(5, 100)
        wall = []
        for j in range(ht):
            total = 0
            row = []
            while total < n:
                if total == n - 1:
                    brick = 1
                else:
                    brick = random.randint(1, min(20, n - total))
                row.append(brick)
                total += brick
            wall.append(row)
        yield (wall, )        

def flatten_generator(seed):
    random.seed(seed)
    for i in range(10000):
        items = create_list(1 + i % 8)
        yield (items, )

def __create_random_word__(n):
    result = ""
    for i in range(n):
        result += chr(ord('a') + random.randint(0, 25))
    return result

def break_into_syllables_generator(seed):
    random.seed(seed)
    for i in range(1000):
        word = __create_random_word__(5 + (i % 15))
        splits = [random.randint(0, len(word) - 1) for i in range(1 + len(word)//2)]
        syllables = [word[i:i+random.randint(1, 6)] for i in splits]
        syllables.extend([__create_random_word__(1+random.randint(0, 4)) for i in range(1 + len(word)//2)])
        random.shuffle(syllables)
        yield (word, syllables)

def scrabble_value_generator(seed):
    random.seed(seed)
    f = open('words.txt', 'r', encoding='utf-8')
    words = [x.strip() for x in f if x.islower()]
    f.close()
    words = limited_alphabet(words, "abcdefghijklmnopqrstuvwxyz")
    for word in words:
        yield[word, [random.randint(1, 3) for i in range(len(word))]]

def expand_intervals_generator(seed):
    random.seed(seed)
    for j in range(1000):
        curr = 0
        result = ""
        first = True
        n = random.randint(1, 20)
        for i in range(n):
            if not first:
                result += ","
            first = False
            if random.randint(0, 99) < 20:
                result += str(curr)
                curr += random.randint(1, 10)
            else:
                end = curr + random.randint(1, 30)
                result += str(curr) + "-" + str(end)
                curr = end + random.randint(1, 10)
        yield (result,)

def collapse_intervals_generator(seed):
    random.seed(seed)
    for i in range(1000):
        items = []
        curr = 1
        n = random.randint(1, 20)
        for j in range(n):
            m = random.randint(1, 5)
            for k in range(m):
                items.append(curr)
                curr += 1
            curr += random.randint(1, 10)
        yield (items,)

def recaman_generator():
    yield (1000000,)

def __no_repeated_digits__(n, allowed):
    n = str(n)
    for i in range(4):
        if n[i] not in allowed:
            return False
        for j in range(i+1, 4):
            if n[i] == n[j]:
                return False
    return True    

def bulls_and_cows_generator(seed):
    random.seed(seed)
    for i in range(100):
        result = []
        n = random.randint(1, 4)
        allowed = random.sample("123456789", 6)
        while len(result) < n:
            guess = random.randint(1000, 9999)
            if __no_repeated_digits__(guess, allowed):
                bulls = random.randint(0, 3)
                cows = random.randint(0, 3)
                cows = min(cows, 4 - bulls)
                if not(bulls == 3 and cows == 1):
                    result.append( (guess, bulls, cows) )
        yield (result,)

def __manhattan__(p1, p2):
    total = 0
    for i in range(len(p1)):
        total += abs(p1[i] - p2[i])
    return total

from math import sqrt

def __euclidean__(p1, p2):
    total = 0
    for i in range(len(p1)):
        total += (p1[i] - p2[i]) * (p1[i] - p2[i])
    return int(sqrt(total))

def farthest_points_distance_generator(seed):
    random.seed(seed)
    dfs = [__euclidean__, __manhattan__]
    for i in range(10000):
        d = random.randint(1, 10)
        n = random.randint(5, 10)
        points = []
        for j in range(n):
            point = tuple([random.randint(-100,100) for k in range(d)])
            points.append(point)
        df = random.choice(dfs)
        yield (points, df)

def contains_bingo_generator(seed):
    random.seed(seed)
    nums = range(1, 99)
    for i in range(10000):
        card = random.sample(nums, 25)
        card = [card[i:i+5] for i in range(0, 25, 5)]
        m = random.randint(20, 80)
        numbers = random.sample(nums, m)
        numbers.sort()
        centerfree = [True, False][random.randint(0,1)]
        yield (card, numbers, centerfree)

def can_balance_generator(seed):
    random.seed(seed)
    for i in range(10000):
        n = random.randint(1, 30)
        items = [random.randint(1,10) for i in range(n)]
        yield (items, )

def calkin_wilf_generator():
    for v in [10, 42, 255, 987, 7654, 12356]:
        yield (v,)

def fibonacci_sum_generator(seed):
    random.seed(seed)
    curr = 1
    while curr < 10 ** 100:
        yield (curr,)
        curr = curr * 2
        curr += random.randint(0, min(curr, 1000))

def create_zigzag_generator(seed):
    random.seed(seed)
    for i in range(10000):
        rows = random.randint(1, 20)
        cols = random.randint(1, 20)
        start = random.randint(1, 100)
        yield (rows, cols, start)

def fibonacci_word_generator(seed):
    random.seed(seed)
    curr = 0
    for i in range(10000):
        yield (curr,)
        curr += random.randint(1, 10)
        curr = curr * 2

def duplicate_word_generator():
    wap = open("warandpeace.txt", encoding='utf-8')
    text = list(wap)
    wap.close()
    for line in text:
        for n in range(1, 14):
            yield (line, n)

def all_cyclic_shifts_generator():
    f = open('words.txt', 'r', encoding='utf-8')
    words = [x.strip() for x in f if x.islower()]
    f.close()
    words = limited_alphabet(words, "abcdefghijklmnopqrstuvwxyz")
    for word in words:
        yield (word,)

def aliquot_sequence_generator():
    for i in range(1, 100):
        yield (i, 10)
        yield (i, 100)

def josephus_generator():
    for n in range(2, 100):
        for k in range(1, n):
            yield (n, k)

def balanced_ternary_generator(seed):
    random.seed(seed)
    curr = 1
    for i in range(1, 1000):
        yield (curr,)
        yield (-curr,)
        curr += random.randint(1, max(3, curr // 10))

__names__ = ["brad", "ben", "britain", "donald", "bill", "ronald",
             "george", "laura", "barbara",
             "barack", "angelina", "jennifer", "ross", "rachel",
             "monica", "phoebe", "joey", "chandler",
             "hillary", "michelle", "melania", "nancy", "homer",
             "marge", "bart", "lisa", "maggie", "waylon", "montgomery",
             "california", "canada", "germany", "sheldon", "leonard",
             "rajesh", "howard", "penny", "amy", "bernadette"]

def brangelina_generator():
    for i in range(len(__names__)):
        for j in range(len(__names__)):
            yield (__names__[i], __names__[j])
            
def frequency_sort_generator(seed):
    random.seed(seed)
    for i in range(1000):
        ln = random.randint(1, 1000)
        elems = [random.randint(1, 2 + ln // 2) for x in range(ln)]
        yield(elems,)

def count_consecutive_summers_generator():
    for i in range(1, 1000):
        yield(i,)

def detab_generator(seed):
    wap = open("warandpeace.txt", encoding='utf-8')
    text = list(wap)
    wap.close()
    random.seed(seed)
    for line in text:
        n = random.randint(1, 7)
        yield (line, n, ' ')

def running_median_of_three_generator(seed):
    random.seed(seed)
    yield ([],)
    yield ([42],)
    for i in range(100):
        n = random.randint(2, 1000)
        items = [random.randint(1, 100) for x in range(n)]
        yield (items,)
        
def iterated_remove_pairs_generator(seed):
    random.seed(seed)
    for k in range(1000):
        n = random.randint(0, 100)
        vals = [random.randint(1, 10000) for i in range(7)]
        items = [vals[random.randint(0, 6)] for i in range(n)]
        yield (items,)

def is_perfect_power_generator(seed):
    random.seed(seed)
    for k in range(500):
        base = random.randint(2, 10)
        exp = random.randint(2, 13 - base)
        off = random.randint(0, 1)
        yield (base ** exp - off, )

def sort_by_digit_count_generator(seed):
    random.seed(seed)
    for k in range(1000):
        n = random.randint(1, 1000)
        yield ([random.randint(1, 10**6) for i in range(n)],)

def count_divisors_in_range_generator(seed):
    random.seed(seed)
    v = 3
    step = 1
    up = 10
    for i in range(100000):
        start = random.randint(-v, v)
        end = random.randint(0, v) + start
        n = random.randint(1, v)
        yield (start, end, n)
        v += step
        if i == up:
            up = 10 * up
            step = step * 10

__players__ = ['anita', 'suzanne', 'suzy', 'tom', 'steve', 'ilkka', 'rajesh',
               'amy', 'penny', 'sheldon', 'leonard', 'bernadette', 'howard']

def highest_n_scores_generator(seed):
    random.seed(seed)
    for i in range(10000):
        scores = [(name, random.randint(1, 100)) for name in __players__\
                  for k in range(random.randint(0, 20))]
        n = random.randint(1, 10)
        yield (scores, n)

# Let the good times roll!

test_all_functions(labs109, [
        (
        "milton_work_point_count",
        milton_work_point_count_generator(12345),
        "478b4f9abb802dcd9c175851e5de90febea421622b851dbb54"        
        ),        
        (
        "highest_n_scores",
        highest_n_scores_generator(12345),
        "978ce1599544e991c1cdc5824a762ffbed54ebcee76ca87821"      
        ),
        (
        "count_divisors_in_range",        
        count_divisors_in_range_generator(12345),
        "046f15a3e3a38735d04736da74262a54f7c6882c61b3e4db5a"
        ),
        (
        "sort_by_digit_count",
        sort_by_digit_count_generator(12345),
        "faa4547a1a4fc27a0e8c16c1f1d4f8d6385587ab08e9c9d0c5"        
        ),
        (
        "is_perfect_power",                
        is_perfect_power_generator(12345),
        "5c396434e95e5899055195e80660137588f6d81c3cf6594d32"
        ),        
        (
        "iterated_remove_pairs",
        iterated_remove_pairs_generator(12345),
        "f3d6588ec3c251abfc024698c2a7371dcc7e175af1e41bb0aa"
        ),
        (
        "detab",
        detab_generator(12345),
        "d3e7eea790490fd172a01cdf48639aad2462d7f440fe68cba4"
        ),
        (
        "running_median_of_three",
        running_median_of_three_generator(12345),
        "4325b7bb7172d5a4f7e478174661d109aea0de9bba3480536d"        
        ),
        (
        "frequency_sort",
        frequency_sort_generator(12345),
        "608f5351a1e77413aff8779d4586ca536eb5314e686892b391"
        ),
        (
        "count_consecutive_summers",         
        count_consecutive_summers_generator(),
        "3ade63a194b40ff5aa1b53642eee754d30f2ab48ef77330540"
        ),
        (
        "brangelina",
        brangelina_generator(),
        "fdbbfd7aa2ebcb989862f4e23defc6cafd4aca55ce3235a463"
        ),        
        (
        "balanced_ternary",
        balanced_ternary_generator(12345),
        "08dcda71f136c16362cc53e62f98d49b28bb45c43ddee4ea32"        
        ),
        (
        "josephus",
        josephus_generator(),
        "3ff6a944f6f48e41cc53a7013e785da77be27c7372b4a4cdbb"
        ),
        (
        "aliquot_sequence",
        aliquot_sequence_generator(),
        "5942bb5b3dc190eaddff33df990de03666441706387cde0d7e"        
        ),        
        (
        "all_cyclic_shifts",
        all_cyclic_shifts_generator(),
        "0890c1b6077f0ec28642ab7723ba49e6453f0d7251a25e9e5a"                
        ),        
        (
        "duplicate_word",
        duplicate_word_generator(),
        "aa182f216a2d696bdebd03eb2f01400dcc9322e31e302471d7"        
        ),        
        (
        "fibonacci_word",
        fibonacci_word_generator(12345),
        "275ac5dc13b0bf5364bb25fca249b2115357fc7666154d1cd6"               
        ),        
        (
        "create_zigzag",
        create_zigzag_generator(12345),
        "e3376a7132fe7ed1b04f38215dea836d70e8cf8d0e316868cf"                
        ),        
        (
        "fibonacci_sum",
        fibonacci_sum_generator(12345),
        "c4052229fe7b1abf54e3d0757ed2d27777b9323fb753127cf9"
        ),        
        (
        "calkin_wilf",
        calkin_wilf_generator(),
        "e5ff0851c0830b72802a818eeaec66711b6e3b91a004263674"                
        ),        
        (
        "can_balance",
        can_balance_generator(12345),
        "0d79528d49fc77f06d98f3d2672306097a1aacfcb65e050f6a"        
        ),
        (
        "contains_bingo",
        contains_bingo_generator(12345),
        "c352ce01918d0d47ca13adedf25556e5fd4ab1f672e07bc52f"
        ),        
        (
        "farthest_points_distance",
        farthest_points_distance_generator(12345),
        "2bc835828a4967b35bf1c022fc4c204e2fdc955c03947f3a2b"
        ),
        (
        "bulls_and_cows",
        bulls_and_cows_generator(12345),
        "e00ca4cd1996a51ef5cd5588a7facd0a00f2e3f3946d5f4e96"               
        ),        
        (
        "recaman",
        recaman_generator(),
        "48f7b14610fe8f54ab2b1d81265847eec47d450d13e4a4c6c5"
        ),
        (
        "collapse_intervals",
        collapse_intervals_generator(12345),
        "bb95484119b5e00b704121baa1f7ef5312154ad542cf9da828"
        ),        
        (
        "expand_intervals",
        expand_intervals_generator(12345),
        "9fecebbd937380814f804508ed3f491a6a0c353050e60a3d60"
        ),        
        (
        "scrabble_value",        
        scrabble_value_generator(12345),
        "398a3bd44dbc4cf3116e25e52db44809c7cad86ddb03eb0186"
        ),
        (
        "break_into_syllables",                
        break_into_syllables_generator(12345),
        "d3b84c8f7387becbb82a17b15989066231983a7947745581f9"
        ),        
        (
        "reverse_ascending_sublists",
        reverse_ascending_sublists_generator(12345),
        "78fed45a9925dd87964e1433e1db5451900de41a491f2b8144"
        ),        
        (
        "flatten",
        flatten_generator(12345),
        "965fda78b5ad7ae3924edf4b545c84b6d5a78158d92b234f65"                
        ),        
        (
        "brick_wall",
        brick_wall_generator(12345),
        "1927b926398675551013143c95658f8f9d8123d1990fc1d117"        
        ),
        (
        "reverse_reversed",       
        reverse_reversed_generator(12345),
        "c3ec2d6688cc38e8ad384ed5cbf5dabc663dbf9e97d7608367"
        ),
        (
        "longest_palindrome",
        longest_palindrome_generator(12345),
        "3dd73f155d4e4debbcaba8a2815479ecf42f528ec577173a63"        
        ),
        (
        "group_equal",
        group_equal_generator(12345),
        "242fac179412d7ad82bebadbd74ac7d0044b33942a714870b9"
        ),        
        (
        "postfix_evaluate",
        postfix_evaluate_generator(99),
        "6a37236b142ad06ab0e3f97cf2733c831eeab1f9463c819e97"
        ),                     
        (
        "letter_pair_freqs",
        letter_pair_freqs_generator(),
        "e18e2c32dc977e5647fc11af704cc98bfe8e994782349c4cd4"                
        ),
        (
        "paragraph_lengths",
        paragraph_lengths_generator(),
        "df303673536dce13da7c626b2a07ba949cd62388761d98b68d"        
        ),
        (
        "ryerson_letter_grade",        
        ryerson_letter_grade_generator(),
        "b9b86a019c4502be825b0ed52c187f9a29106a08fbbb1ffcc6"
        ),
        (
        "is_ascending",        
        is_ascending_generator(7),
        "4c5f0dbf663f3350b7cf3d16f0589fc7dc5168ca17e4aefd3f"
        ),
        (
        "double_until_all_digits",
        double_until_all_digits_generator(),
        "7c4ba46364765cb0679f609d428bbbae8ba0df440b001c4162"
        ),
        (
        "caps_lock_stuck",
        caps_lock_stuck_generator(),
        "4aad29b868200851957f4e59a51321d5be077c1217f66ca1b9"        
        ),
        (
        "give_change",
        give_change_generator(12345),
        "e8419a56ab09d1cf1effb2bb9c45802ae21a2304793cc8a892"
        ),
        (
        "winning_card",
        winning_card_generator(12345),
        "32c7fee1415a8095db6f318ad293dd08dec4e6904f304c4a73"
        ),
        (
        "hand_is_badugi",
        hand_is_badugi_generator(987),
        "d37917aab58ce06778d3f667f6c348d1e30ee67271d9d1de60"
        ),
        (
        "bridge_hand_shape",
        bridge_hand_shape_generator(12345),
        "61cfd31019c2838780311603caee80a9c57fae37d4f5b561ce"       
        ),
        (
        "hand_shape_distribution",
        hand_shape_distribution_generator(12345),
        "0a34b7e0409552587469623bd8609dae1218f909c178c592db"      
        ),
        (
        "sort_by_typing_handedness",
        sort_by_typing_handedness_generator(),
        "c093675bb9814e5a2a761c829e8fb5b3a714e93ea2031fd1c3"       
        ),
        (
        "word_salad",
        word_salad_generator(12345),
        "9f4b64f15b92814a5bba3e3c422e0ed74fc8fb802ccb9b004b"                
        ),        
        (
        "possible_words",
        possible_words_generator(999),                
        "55e494a37554d8f8b2c98bd7451de2b05728aa66be210478cd"
        ),   
], "labs109.py")