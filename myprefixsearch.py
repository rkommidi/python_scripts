# Problem Name is &&& Prefix Search &&& PLEASE DO NOT REMOVE THIS LINE.
import time

"""
  Instructions to candidate.
  1) Run this code in the REPL to observe its behaviour.
  2) Provide an implementation of the find_all method in MyPrefixSearch.
  3) Describe any trade-offs arising from your implementation.
  4) If time permits, try to improve your implementation.
"""

class MyPrefixSearch:
    document = "";

    def __init__(self, document):
        self.document = document;

    """
    find_all: Return a list of all locations in a document where the
    (case insensitive) word begins with the given prefix.

    Example:  given the document "a aa Aaa abca bca",
      1) find_all("a")   -> [0, 2, 5, 9]
      2) find_all("bc")  -> [14]
      3) find_all("aA")  -> [2, 5]
      4) find_all("abc") -> [9]

    """
    def find_all(self, prefix):
        # TODO implement this
        
        result = []
        idx = 0
        prefix_length = len(prefix)
        #print(prefix)
        
        if prefix_length == 0:
            return []
        
        for word in self.document.split(" "):
            #print(word, prefix)
            word_length = len(word)
            if word_length > prefix_length:
                 compare_word = word.lower()[0:prefix_length] 
            else:
                compare_word = word.lower()
                
            if compare_word== prefix.lower():
               # print(word, prefix)
                result.append(idx)
                
            idx += len(word)+1
            
        print(result)
                
        return result


###########  Tests  ###########

DOCUMENT = ("In publishing and graphic design, lorem ipsum is a "
"filler text commonly used to demonstrate the graphic elements of a "
"document or visual presentation. Replacing meaningful content that "
"could be distracting with placeholder text may allow viewers to focus "
"on graphic aspects such as font, typography, and page layout. It also "
"reduces the need for the designer to come up with meaningful text, as "
"they can instead use hastily generated lorem ipsum text. The lorem "
"ipsum text is typically a scrambled section of De finibus bonorum et "
"malorum, a 1st-century BC Latin text by Cicero, with words altered, "
"added, and removed to make it nonsensical, improper Latin. A variation "
"of the ordinary lorem ipsum text has been used in typesetting since "
"the 1960s or earlier, when it was popularized by advertisements for "
"Letraset transfer sheets. It was introduced to the Information Age in "
"the mid-1980s by Aldus Corporation, which employed it in graphics and "
"word processing templates for its desktop publishing program, "
"PageMaker, for the Apple Macintosh. A common form of lorem ipsum "
"reads: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
"eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad "
"minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
"aliquip ex ea commodo consequat. Duis aute irure dolor in "
"reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
"pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
"culpa qui officia deserunt mollit anim id est laborum.")


"""
Validate that the prefix search returns the correct results for the sample document.
"""
def do_tests_pass():
    prefix_search = MyPrefixSearch(DOCUMENT);

    if (prefix_search.find_all("demonstrate")  == [ 80 ]
      and prefix_search.find_all("pub")        == [ 3, 988 ]
      and prefix_search.find_all("publishing") == [ 3, 988 ]
      and prefix_search.find_all("lab")     == [ 1173, 1263, 1517 ]
      and prefix_search.find_all("laborum") == [ 1517 ]
      and prefix_search.find_all("in") == [ 0, 404, 717, 839, 857, 873, 930, 1159, 1334, 1351, 1468]
      and prefix_search.find_all("lor")== [ 34, 434, 456, 686, 1061, 1080 ]
      and prefix_search.find_all("l")  == [ 34, 309, 434, 456, 557, 651, 686, 806, 1061, 1080, 1173, 1263, 1517]
      and prefix_search.find_all("hamburger")   == []
      and prefix_search.find_all("")   == []):
        print("All Tests Pass")
    else:
        print("Test Fails")

if __name__ == "__main__":
    do_tests_pass()

