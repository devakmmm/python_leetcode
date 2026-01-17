const roadmap = [
  {
    id: "arrays",
    title: "Arrays & Hashing",
    stage: "Foundations",
    focus: "Count, map, and detect duplicates quickly.",
    lessons: [
      {
        id: "contains-duplicate",
        title: "Contains Duplicate",
        difficulty: "Easy",
        summary: "Use a set to detect a repeat in one pass.",
        goal: "Return true if any number appears at least twice.",
        approach:
          "Track seen numbers in a set. If a number is already in the set, return true.",
        example: "nums = [1, 2, 3, 1] => true",
        starter: "def contains_duplicate(nums):\n    pass",
        steps: [
          "Create an empty set named seen to record numbers already visited.",
          "Loop through each number in nums from left to right.",
          "If the number is already in seen, return True because a duplicate exists.",
          "Otherwise add the number to seen and continue.",
          "After the loop finishes, return False.",
        ],
        complexity: "Time O(n), Space O(n).",
      },
      {
        id: "valid-anagram",
        title: "Valid Anagram",
        difficulty: "Easy",
        summary: "Count letters and compare frequency maps.",
        goal: "Return true if two strings are anagrams.",
        approach:
          "Count characters in both strings using a dictionary. The maps must match.",
        example: "s = 'anagram', t = 'nagaram' => true",
        starter: "def is_anagram(s, t):\n    pass",
        steps: [
          "If the lengths differ, return False immediately.",
          "Create a dictionary counts to store character frequencies for s.",
          "Loop through s and increment counts for each character.",
          "Loop through t and decrement counts; if a char is missing, return False.",
          "If a count reaches zero, remove that key to keep the map clean.",
          "At the end, return True only if counts is empty.",
        ],
        complexity: "Time O(n), Space O(1) for fixed alphabet.",
      },
      {
        id: "two-sum",
        title: "Two Sum",
        difficulty: "Easy",
        summary: "Store complements in a hash map.",
        goal: "Return indices of two numbers that add to target.",
        approach:
          "Scan left to right. For each value, check if its complement was seen.",
        example: "nums = [2, 7, 11, 15], target = 9 => [0, 1]",
        starter: "def two_sum(nums, target):\n    pass",
        steps: [
          "Create a dictionary seen to map value to index.",
          "Loop through nums with index i and value n.",
          "Compute complement = target - n.",
          "If complement is in seen, return [seen[complement], i].",
          "Otherwise store seen[n] = i and keep going.",
          "If no pair is found, return an empty list.",
        ],
        complexity: "Time O(n), Space O(n).",
      },
    ],
  },
  {
    id: "two-pointers",
    title: "Two Pointers",
    stage: "Foundations",
    focus: "Shrink or expand ranges without extra space.",
    lessons: [
      {
        id: "valid-palindrome",
        title: "Valid Palindrome",
        difficulty: "Easy",
        summary: "Skip non-alphanumerics and compare ends.",
        goal: "Return true if a string is a palindrome ignoring punctuation.",
        approach:
          "Use left and right pointers. Move inward while skipping non-letters/digits.",
        example: "s = 'A man, a plan, a canal: Panama' => true",
        starter: "def is_palindrome(s):\n    pass",
        steps: [
          "Set left at the start and right at the end of the string.",
          "While left < right, move left forward past non-alphanumeric chars.",
          "Move right backward past non-alphanumeric chars.",
          "Compare lowercase s[left] and s[right]; if they differ, return False.",
          "Move both pointers inward and continue.",
          "If the loop ends, return True.",
        ],
        complexity: "Time O(n), Space O(1).",
      },
      {
        id: "two-sum-ii",
        title: "Two Sum II",
        difficulty: "Medium",
        summary: "Move pointers based on sum vs target.",
        goal: "Find two numbers in a sorted array that sum to target.",
        approach:
          "Start at both ends. Increase left if sum is small, decrease right if big.",
        example: "numbers = [2, 7, 11, 15], target = 9 => [1, 2]",
        starter: "def two_sum_sorted(numbers, target):\n    pass",
        steps: [
          "Set left = 0 and right = len(numbers) - 1.",
          "While left < right, compute the current sum.",
          "If sum equals target, return [left + 1, right + 1].",
          "If sum is too small, move left rightward to increase it.",
          "If sum is too large, move right leftward to decrease it.",
          "If pointers cross, return an empty list.",
        ],
        complexity: "Time O(n), Space O(1).",
      },
      {
        id: "three-sum",
        title: "3Sum",
        difficulty: "Medium",
        summary: "Fix one value, then two-pointer scan.",
        goal: "Return unique triplets that sum to zero.",
        approach:
          "Sort the array, then for each index, use two pointers to find pairs.",
        example: "nums = [-1, 0, 1, 2, -1, -4] => [[-1, -1, 2], [-1, 0, 1]]",
        starter: "def three_sum(nums):\n    pass",
        steps: [
          "Sort nums so duplicates are adjacent and two pointers can be used.",
          "For each index i, skip if nums[i] equals nums[i - 1] to avoid repeats.",
          "Set left = i + 1 and right = last index.",
          "Compute total = nums[i] + nums[left] + nums[right].",
          "If total is zero, record the triplet and move both pointers, skipping duplicates.",
          "If total is too small, move left rightward; if too large, move right leftward.",
          "Continue until pointers meet, then move to the next i.",
        ],
        complexity: "Time O(n^2), Space O(1) extra.",
      },
    ],
  },
  {
    id: "sliding-window",
    title: "Sliding Window",
    stage: "Core",
    focus: "Track window state as you move through arrays.",
    lessons: [
      {
        id: "best-time",
        title: "Best Time to Buy and Sell Stock",
        difficulty: "Easy",
        summary: "Track minimum price and best profit.",
        goal: "Return the max profit from one buy and one sell.",
        approach:
          "Keep a running minimum price, update profit with current price.",
        example: "prices = [7, 1, 5, 3, 6, 4] => 5",
        starter: "def max_profit(prices):\n    pass",
        steps: [
          "Track min_price as the lowest price seen so far.",
          "Track best as the maximum profit seen so far.",
          "For each price, update min_price if the price is lower.",
          "Compute profit = price - min_price and update best if larger.",
          "Return best at the end.",
        ],
        complexity: "Time O(n), Space O(1).",
      },
      {
        id: "longest-substring",
        title: "Longest Substring Without Repeating",
        difficulty: "Medium",
        summary: "Move left pointer after duplicates.",
        goal: "Return length of longest substring with unique chars.",
        approach:
          "Store last seen index, update left pointer when duplicate appears.",
        example: "s = 'abcabcbb' => 3",
        starter: "def length_of_longest_substring(s):\n    pass",
        steps: [
          "Use a dictionary last_seen for character -> most recent index.",
          "Maintain left pointer for the current window and best length so far.",
          "For each right index and character, check if it was seen inside the window.",
          "If yes, move left to last_seen[char] + 1 to remove the duplicate.",
          "Update last_seen for the current character.",
          "Update best with the current window size.",
          "Return best after the loop.",
        ],
        complexity: "Time O(n), Space O(n).",
      },
      {
        id: "permutation-in-string",
        title: "Permutation in String",
        difficulty: "Medium",
        summary: "Compare window counts to target counts.",
        goal: "Return true if s2 contains a permutation of s1.",
        approach:
          "Use a sliding window of length len(s1) and match counts.",
        example: "s1 = 'ab', s2 = 'eidbaooo' => true",
        starter: "def check_inclusion(s1, s2):\n    pass",
        steps: [
          "If s1 is longer than s2, return False.",
          "Build a frequency map need for s1.",
          "Use a window frequency map and a left pointer.",
          "Expand right by adding s2[right] to the window map.",
          "If window size exceeds len(s1), shrink by removing s2[left] and increment left.",
          "When window size equals len(s1), compare window and need; if equal return True.",
          "If the loop ends, return False.",
        ],
        complexity: "Time O(n), Space O(1) for fixed alphabet.",
      },
    ],
  },
  {
    id: "stack",
    title: "Stack",
    stage: "Core",
    focus: "Match pairs and simulate recursion.",
    lessons: [
      {
        id: "valid-parentheses",
        title: "Valid Parentheses",
        difficulty: "Easy",
        summary: "Use a stack to match brackets.",
        goal: "Return true if brackets close in correct order.",
        approach:
          "Push opening brackets, pop on close and compare types.",
        example: "s = '()[]{}' => true",
        starter: "def is_valid(s):\n    pass",
        steps: [
          "Create a stack and a map of closing brackets to opening brackets.",
          "Loop through each character in the string.",
          "If it is a closing bracket, check the stack top matches; otherwise return False.",
          "If it is an opening bracket, push it onto the stack.",
          "At the end, return True only if the stack is empty.",
        ],
        complexity: "Time O(n), Space O(n).",
      },
      {
        id: "min-stack",
        title: "Min Stack",
        difficulty: "Medium",
        summary: "Store min value alongside each push.",
        goal: "Support push, pop, top, and getMin in O(1).",
        approach:
          "Each stack entry keeps the value and the min so far.",
        example: "push 3, push 1, min => 1",
        starter: "class MinStack:\n    pass",
        steps: [
          "Store each push as a pair: (value, min_so_far).",
          "On push, compute min_so_far using the previous minimum.",
          "On pop, remove the top pair.",
          "On top, return the value from the top pair.",
          "On get_min, return the min_so_far from the top pair.",
        ],
        complexity: "Time O(1) per op, Space O(n).",
      },
      {
        id: "eval-rpn",
        title: "Evaluate Reverse Polish Notation",
        difficulty: "Medium",
        summary: "Compute when an operator appears.",
        goal: "Evaluate an RPN expression.",
        approach:
          "Use a stack; pop two numbers for each operator.",
        example: "tokens = ['2', '1', '+', '3', '*'] => 9",
        starter: "def eval_rpn(tokens):\n    pass",
        steps: [
          "Create an empty stack.",
          "Scan tokens left to right.",
          "If the token is an operator, pop two numbers and apply the operator.",
          "Push the computed result back onto the stack.",
          "If the token is a number, convert to int and push it.",
          "After processing all tokens, return the top of the stack.",
        ],
        complexity: "Time O(n), Space O(n).",
      },
    ],
  },
  {
    id: "binary-search",
    title: "Binary Search",
    stage: "Core",
    focus: "Use sorted structure to cut search space.",
    lessons: [
      {
        id: "binary-search",
        title: "Binary Search",
        difficulty: "Easy",
        summary: "Classic mid check with two pointers.",
        goal: "Return the index of target in a sorted list.",
        approach:
          "Compare mid to target and adjust left or right bounds.",
        example: "nums = [-1,0,3,5,9,12], target = 9 => 4",
        starter: "def search(nums, target):\n    pass",
        steps: [
          "Set left = 0 and right = len(nums) - 1.",
          "While left <= right, compute mid.",
          "If nums[mid] equals target, return mid.",
          "If nums[mid] is less than target, move left to mid + 1.",
          "Otherwise move right to mid - 1.",
          "If not found, return -1.",
        ],
        complexity: "Time O(log n), Space O(1).",
      },
      {
        id: "search-rotated",
        title: "Search in Rotated Array",
        difficulty: "Medium",
        summary: "Find sorted half and decide where to search.",
        goal: "Return index of target in rotated sorted array.",
        approach:
          "At each step, one half is sorted. Decide which half contains target.",
        example: "nums = [4,5,6,7,0,1,2], target = 0 => 4",
        starter: "def search_rotated(nums, target):\n    pass",
        steps: [
          "Set left = 0 and right = len(nums) - 1.",
          "While left <= right, compute mid.",
          "If nums[mid] equals target, return mid.",
          "Determine which half is sorted by comparing nums[left] and nums[mid].",
          "If target is within the sorted half, move into that half; otherwise search the other half.",
          "If not found, return -1.",
        ],
        complexity: "Time O(log n), Space O(1).",
      },
      {
        id: "min-rotated",
        title: "Find Min in Rotated Array",
        difficulty: "Medium",
        summary: "Shrink toward the unsorted half.",
        goal: "Return the minimum in a rotated sorted array.",
        approach:
          "Compare mid with right. If mid is bigger, min is to the right.",
        example: "nums = [3,4,5,1,2] => 1",
        starter: "def find_min(nums):\n    pass",
        steps: [
          "Set left = 0 and right = len(nums) - 1.",
          "While left < right, compute mid.",
          "If nums[mid] > nums[right], the minimum is to the right; move left = mid + 1.",
          "Otherwise the minimum is at mid or to the left; move right = mid.",
          "Return nums[left].",
        ],
        complexity: "Time O(log n), Space O(1).",
      },
    ],
  },
  {
    id: "linked-list",
    title: "Linked List",
    stage: "Core",
    focus: "Pointer moves and reversing links.",
    lessons: [
      {
        id: "reverse-list",
        title: "Reverse Linked List",
        difficulty: "Easy",
        summary: "Iterative pointer reversal.",
        goal: "Reverse a singly linked list.",
        approach:
          "Move through nodes, rewire next pointers using prev/current.",
        example: "1 -> 2 -> 3 => 3 -> 2 -> 1",
        starter: "def reverse_list(head):\n    pass",
        steps: [
          "Initialize prev = None and curr = head.",
          "While curr is not None, save next = curr.next.",
          "Reverse the link by setting curr.next = prev.",
          "Move prev to curr and curr to next.",
          "Return prev as the new head.",
        ],
        complexity: "Time O(n), Space O(1).",
      },
      {
        id: "merge-two",
        title: "Merge Two Sorted Lists",
        difficulty: "Easy",
        summary: "Iterate with a dummy head.",
        goal: "Merge two sorted linked lists.",
        approach:
          "Use a dummy node and attach the smaller head each step.",
        example: "1->2->4 and 1->3->4 => 1->1->2->3->4->4",
        starter: "def merge_two_lists(l1, l2):\n    pass",
        steps: [
          "Create a dummy node and set tail to it.",
          "While both lists have nodes, compare their values.",
          "Attach the smaller node to tail and advance that list.",
          "Advance tail.",
          "Attach any remaining nodes after the loop.",
          "Return dummy.next.",
        ],
        complexity: "Time O(n+m), Space O(1).",
      },
      {
        id: "linked-cycle",
        title: "Linked List Cycle",
        difficulty: "Easy",
        summary: "Use slow and fast pointers.",
        goal: "Return true if a linked list has a cycle.",
        approach:
          "Move slow by 1 and fast by 2. If they meet, there is a cycle.",
        example: "head = [3,2,0,-4], pos = 1 => true",
        starter: "def has_cycle(head):\n    pass",
        steps: [
          "Set slow and fast to head.",
          "While fast and fast.next exist, move slow by 1 and fast by 2.",
          "If slow == fast, a cycle exists; return True.",
          "If the loop ends, return False.",
        ],
        complexity: "Time O(n), Space O(1).",
      },
    ],
  },
  {
    id: "trees",
    title: "Trees",
    stage: "Core",
    focus: "Traverse and build recursion intuition.",
    lessons: [
      {
        id: "invert-tree",
        title: "Invert Binary Tree",
        difficulty: "Easy",
        summary: "Swap left and right recursively.",
        goal: "Return a tree with left and right swapped at every node.",
        approach:
          "Swap children and recurse down the tree.",
        example: "[4,2,7,1,3,6,9] => [4,7,2,9,6,3,1]",
        starter: "def invert_tree(root):\n    pass",
        steps: [
          "If root is None, return None.",
          "Swap root.left and root.right.",
          "Recursively invert the left subtree.",
          "Recursively invert the right subtree.",
          "Return root.",
        ],
        complexity: "Time O(n), Space O(h).",
      },
      {
        id: "max-depth",
        title: "Max Depth of Binary Tree",
        difficulty: "Easy",
        summary: "Depth is 1 + max(depth(left), depth(right)).",
        goal: "Return the maximum depth of a binary tree.",
        approach:
          "Recursive DFS to compute depths for children.",
        example: "root = [3,9,20,null,null,15,7] => 3",
        starter: "def max_depth(root):\n    pass",
        steps: [
          "If root is None, return 0.",
          "Compute left_depth and right_depth recursively.",
          "Return 1 + max(left_depth, right_depth).",
        ],
        complexity: "Time O(n), Space O(h).",
      },
      {
        id: "validate-bst",
        title: "Validate BST",
        difficulty: "Medium",
        summary: "Keep bounds as you traverse.",
        goal: "Return true if a binary tree is a valid BST.",
        approach:
          "DFS while carrying lower/upper limits for valid node values.",
        example: "root = [2,1,3] => true",
        starter: "def is_valid_bst(root):\n    pass",
        steps: [
          "Create a DFS helper that accepts a node and value bounds (low, high).",
          "If node is None, return True.",
          "If node.val is not between low and high, return False.",
          "Recurse left with high = node.val and right with low = node.val.",
          "Return True only if both sides are valid.",
        ],
        complexity: "Time O(n), Space O(h).",
      },
    ],
  },
  {
    id: "graphs",
    title: "Graphs",
    stage: "Advanced",
    focus: "Traverse grids and manage dependencies.",
    lessons: [
      {
        id: "num-islands",
        title: "Number of Islands",
        difficulty: "Medium",
        summary: "DFS/BFS to sink each island.",
        goal: "Count islands in a grid of 0s and 1s.",
        approach:
          "When you see land, run DFS to mark the whole island as visited.",
        example: "grid = [['1','1','0'],['1','0','0'],['0','0','1']] => 2",
        starter: "def num_islands(grid):\n    pass",
        steps: [
          "Loop through each cell in the grid.",
          "When you find land ('1'), increment count and start DFS or BFS.",
          "In DFS, stop if out of bounds or the cell is not '1'.",
          "Mark the cell as '0' to avoid revisiting.",
          "Explore up, down, left, and right neighbors.",
          "Return the count after scanning the grid.",
        ],
        complexity: "Time O(r*c), Space O(r*c).",
      },
      {
        id: "clone-graph",
        title: "Clone Graph",
        difficulty: "Medium",
        summary: "DFS with a map of original to clone.",
        goal: "Deep copy an undirected graph.",
        approach:
          "Use a hashmap to avoid copying the same node twice.",
        example: "graph = [[2,4],[1,3],[2,4],[1,3]]",
        starter: "def clone_graph(node):\n    pass",
        steps: [
          "If the input node is None, return None.",
          "Use a map to store original node -> cloned node.",
          "Define DFS: if node already cloned, return it.",
          "Create a clone for the node and add it to the map.",
          "Clone each neighbor recursively and append to clone.neighbors.",
          "Return the clone.",
        ],
        complexity: "Time O(V+E), Space O(V).",
      },
      {
        id: "course-schedule",
        title: "Course Schedule",
        difficulty: "Medium",
        summary: "Detect cycles in a directed graph.",
        goal: "Return true if you can finish all courses.",
        approach:
          "Use DFS with states (unvisited, visiting, visited) to detect a cycle.",
        example: "numCourses = 2, prereq = [[1,0]] => true",
        starter: "def can_finish(num_courses, prereq):\n    pass",
        steps: [
          "Build an adjacency list from prereq pairs.",
          "Use two sets: visiting and visited.",
          "DFS each course: if in visiting, a cycle exists and return False.",
          "If already in visited, return True.",
          "Mark as visiting, DFS prereqs; if any return False, bubble it up.",
          "Move course to visited and return True.",
          "Run DFS for all courses and return True if all pass.",
        ],
        complexity: "Time O(V+E), Space O(V).",
      },
    ],
  },
  {
    id: "dynamic-programming",
    title: "Dynamic Programming",
    stage: "Advanced",
    focus: "Turn recursion into reusable subproblems.",
    lessons: [
      {
        id: "climbing-stairs",
        title: "Climbing Stairs",
        difficulty: "Easy",
        summary: "Fibonacci in disguise.",
        goal: "Count ways to climb to the top.",
        approach:
          "DP: ways[i] = ways[i-1] + ways[i-2].",
        example: "n = 3 => 3",
        starter: "def climb_stairs(n):\n    pass",
        steps: [
          "Handle small n (1 or 2) directly.",
          "Use two variables for ways to reach the previous two steps.",
          "Iterate from 3 to n, compute new = a + b, then shift.",
          "Return the last computed value.",
        ],
        complexity: "Time O(n), Space O(1).",
      },
      {
        id: "house-robber",
        title: "House Robber",
        difficulty: "Medium",
        summary: "Track best with and without current house.",
        goal: "Maximize money without robbing adjacent houses.",
        approach:
          "At each house, choose max of skipping or robbing it.",
        example: "nums = [1,2,3,1] => 4",
        starter: "def rob(nums):\n    pass",
        steps: [
          "Track two values: best up to i-2 (rob1) and best up to i-1 (rob2).",
          "For each house value, compute new_rob = max(rob1 + value, rob2).",
          "Shift rob1 = rob2 and rob2 = new_rob.",
          "Return rob2.",
        ],
        complexity: "Time O(n), Space O(1).",
      },
      {
        id: "lis",
        title: "Longest Increasing Subsequence",
        difficulty: "Medium",
        summary: "DP over prefixes.",
        goal: "Return the length of the LIS.",
        approach:
          "For each index, check previous values and update best length.",
        example: "nums = [10,9,2,5,3,7,101,18] => 4",
        starter: "def length_of_lis(nums):\n    pass",
        steps: [
          "If nums is empty, return 0.",
          "Create dp array initialized to 1 for each index.",
          "For each i, check all j < i.",
          "If nums[j] < nums[i], update dp[i] = max(dp[i], dp[j] + 1).",
          "Return the max value in dp.",
        ],
        complexity: "Time O(n^2), Space O(n).",
      },
    ],
  },
];

const storageKey = "neetcode-roadmap-progress";
const activeKey = "neetcode-roadmap-active";

const state = {
  activeModuleId: localStorage.getItem(activeKey) || roadmap[0].id,
  filter: "all",
  focusLessonId: null,
  scrollToFocus: false,
  progress: loadProgress(),
};

const moduleList = document.getElementById("module-list");
const lessonList = document.getElementById("lesson-list");
const moduleTitle = document.getElementById("module-title");
const moduleStage = document.getElementById("module-stage");
const moduleFocus = document.getElementById("module-focus");
const moduleCount = document.getElementById("module-count");
const statTotal = document.getElementById("stat-total");
const statComplete = document.getElementById("stat-complete");
const statPercent = document.getElementById("stat-percent");
const progressFill = document.getElementById("progress-fill");
const focusTitle = document.getElementById("focus-title");
const focusDetail = document.getElementById("focus-detail");
const focusJump = document.getElementById("focus-jump");
const shuffleFocus = document.getElementById("shuffle-focus");
const startRoadmap = document.getElementById("start-roadmap");

function loadProgress() {
  try {
    return JSON.parse(localStorage.getItem(storageKey)) || {};
  } catch (error) {
    return {};
  }
}

function saveProgress() {
  localStorage.setItem(storageKey, JSON.stringify(state.progress));
}

function escapeHtml(value) {
  return value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function getLessonId(moduleId, lessonId) {
  return `${moduleId}:${lessonId}`;
}

function getLessonProgress(moduleId, lessonId) {
  return Boolean(state.progress[getLessonId(moduleId, lessonId)]);
}

function setLessonProgress(moduleId, lessonId, done) {
  const key = getLessonId(moduleId, lessonId);
  if (done) {
    state.progress[key] = true;
  } else {
    delete state.progress[key];
  }
  saveProgress();
}

function getTotals() {
  let total = 0;
  let completed = 0;
  roadmap.forEach((module) => {
    module.lessons.forEach((lesson) => {
      total += 1;
      if (getLessonProgress(module.id, lesson.id)) {
        completed += 1;
      }
    });
  });
  return { total, completed };
}

function renderStats() {
  const { total, completed } = getTotals();
  statTotal.textContent = total;
  statComplete.textContent = completed;
  const percent = total === 0 ? 0 : Math.round((completed / total) * 100);
  statPercent.textContent = `${percent}%`;
  progressFill.style.width = `${percent}%`;
}

function renderModules() {
  moduleList.innerHTML = roadmap
    .map((module) => {
      const completed = module.lessons.filter((lesson) =>
        getLessonProgress(module.id, lesson.id)
      ).length;
      const total = module.lessons.length;
      return `
        <li class="module ${
          module.id === state.activeModuleId ? "is-active" : ""
        }" data-module-id="${module.id}">
          <div class="module-title">${module.title}</div>
          <div class="module-meta">
            <span>${completed} / ${total} lessons</span>
            <span class="stage-chip">${module.stage}</span>
          </div>
        </li>
      `;
    })
    .join("");
}

function renderLessons() {
  const active = roadmap.find((module) => module.id === state.activeModuleId);
  if (!active) {
    return;
  }
  moduleTitle.textContent = active.title;
  moduleStage.textContent = active.stage;
  moduleFocus.textContent = active.focus;

  const lessons = active.lessons.filter((lesson) => {
    const done = getLessonProgress(active.id, lesson.id);
    if (state.filter === "done") {
      return done;
    }
    if (state.filter === "open") {
      return !done;
    }
    return true;
  });

  const completed = active.lessons.filter((lesson) =>
    getLessonProgress(active.id, lesson.id)
  ).length;
  moduleCount.textContent = `${completed} / ${active.lessons.length}`;

  if (lessons.length === 0) {
    lessonList.innerHTML = `<p>No lessons match this filter.</p>`;
    return;
  }

  lessonList.innerHTML = lessons
    .map((lesson) => {
      const done = getLessonProgress(active.id, lesson.id);
      const lessonKey = getLessonId(active.id, lesson.id);
      const open = state.focusLessonId === lessonKey ? "open" : "";
      return `
        <details class="lesson" data-lesson-id="${lessonKey}" ${open}>
          <summary>
            <label class="check">
              <input type="checkbox" data-task-check="${lessonKey}" ${
        done ? "checked" : ""
      } />
            </label>
            <div class="lesson-title">
              <h3>${lesson.title}</h3>
              <p>${lesson.summary}</p>
            </div>
            <span class="tag">${lesson.difficulty}</span>
          </summary>
          <div class="lesson-body">
            <div class="lesson-grid">
              <div>
                <h4>Goal</h4>
                <p>${lesson.goal}</p>
              </div>
              <div>
                <h4>Approach</h4>
                <p>${lesson.approach}</p>
              </div>
              <div>
                <h4>Example</h4>
                <p>${lesson.example}</p>
              </div>
              <div>
                <h4>Complexity</h4>
                <p>${lesson.complexity}</p>
              </div>
            </div>
            ${renderSteps(lesson.steps)}
            ${renderCode("Starter", lesson.starter)}
          </div>
        </details>
      `;
    })
    .join("");

  if (state.focusLessonId && state.scrollToFocus) {
    const target = document.querySelector(
      `[data-lesson-id="${state.focusLessonId}"]`
    );
    if (target) {
      target.scrollIntoView({ behavior: "smooth", block: "start" });
      state.scrollToFocus = false;
    }
  }
}

function renderCode(label, code) {
  return `
    <div>
      <h4>${label}</h4>
      <pre class="code-block"><code>${escapeHtml(code)}</code></pre>
    </div>
  `;
}

function renderSteps(steps) {
  const items = Array.isArray(steps) ? steps : [];
  if (!items.length) {
    return `
      <div>
        <h4>Guided Steps</h4>
        <p>No guided steps available yet.</p>
      </div>
    `;
  }
  const list = items
    .map((step) => `<li>${escapeHtml(step)}</li>`)
    .join("");
  return `
    <div>
      <h4>Guided Steps</h4>
      <ol class="step-list">${list}</ol>
    </div>
  `;
}

function renderFocus(forceNew = false) {
  const openLessons = [];
  const allLessons = [];

  roadmap.forEach((module) => {
    module.lessons.forEach((lesson) => {
      const lessonKey = getLessonId(module.id, lesson.id);
      const entry = {
        lessonKey,
        moduleId: module.id,
        moduleTitle: module.title,
        title: lesson.title,
        summary: lesson.summary,
      };
      allLessons.push(entry);
      if (!getLessonProgress(module.id, lesson.id)) {
        openLessons.push(entry);
      }
    });
  });

  const findLesson = (key) => allLessons.find((lesson) => lesson.lessonKey === key);
  let choice = !forceNew && state.focusLessonId ? findLesson(state.focusLessonId) : null;

  if (choice && openLessons.length) {
    const isDone = !openLessons.find((lesson) => lesson.lessonKey === choice.lessonKey);
    if (isDone) {
      choice = null;
    }
  }

  const pickFrom = openLessons.length ? openLessons : allLessons;

  if (!choice) {
    choice = pickFrom[Math.floor(Math.random() * pickFrom.length)];
  }

  if (!choice) {
    focusTitle.textContent = "No lessons found";
    focusDetail.textContent = "Add lessons to the roadmap to begin.";
    focusJump.disabled = true;
    return;
  }

  state.focusLessonId = choice.lessonKey;
  focusJump.disabled = false;
  focusTitle.textContent = `${choice.title} (${choice.moduleTitle})`;
  focusDetail.textContent = choice.summary;
  focusJump.dataset.moduleId = choice.moduleId;
}

function render() {
  renderStats();
  renderModules();
  renderFocus();
  renderLessons();
}

moduleList.addEventListener("click", (event) => {
  const item = event.target.closest(".module");
  if (!item) {
    return;
  }
  state.activeModuleId = item.dataset.moduleId;
  state.focusLessonId = null;
  localStorage.setItem(activeKey, state.activeModuleId);
  render();
});

lessonList.addEventListener("change", (event) => {
  const input = event.target;
  if (!input.matches("[data-task-check]")) {
    return;
  }
  const [moduleId, lessonId] = input.dataset.taskCheck.split(":");
  setLessonProgress(moduleId, lessonId, input.checked);
  render();
});

const filters = document.querySelectorAll(".filter");
filters.forEach((button) => {
  button.addEventListener("click", () => {
    filters.forEach((btn) => btn.classList.remove("is-active"));
    button.classList.add("is-active");
    state.filter = button.dataset.filter;
    render();
  });
});

shuffleFocus.addEventListener("click", () => {
  renderFocus(true);
});

focusJump.addEventListener("click", () => {
  if (!state.focusLessonId) {
    return;
  }
  const moduleId = focusJump.dataset.moduleId || roadmap[0].id;
  state.activeModuleId = moduleId;
  localStorage.setItem(activeKey, state.activeModuleId);
  state.scrollToFocus = true;
  render();
});

startRoadmap.addEventListener("click", () => {
  state.activeModuleId = roadmap[0].id;
  localStorage.setItem(activeKey, state.activeModuleId);
  state.filter = "all";
  filters.forEach((btn) => btn.classList.remove("is-active"));
  filters[0].classList.add("is-active");
  render();
});

render();
