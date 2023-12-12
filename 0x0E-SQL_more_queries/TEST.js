const removeDuplicates = function (string) {
  let stack = [];
  let x = 0;
  for (let char of string) {
    if (stack[stack.length - 1] === char) stack.pop();
    else stack.push(char);
    x++;
  }
  return stack.join('');
};
console.log(removeDuplicates('abbaca'));
/*
[]
 */
function binary(nums, target) {
  let left = 0,
    right = nums.length - 1;
  while (left <= right) {
    let mid = left + Math.floor((right - left) / 2);
    if (nums[mid] === target) return mid;

    if (nums[mid] > target) right = mid - 1;
    else left = mid + 1;
    console.log(left, right, mid);
    console.log('-----');
  }

  return left;
}
//left = 5 , right =6
console.log(binary([1, 2, 3, 5, 6], 4));
console.log('***');
const moveZeroes = function (nums) {
  let left = 0;
  let right = 0;

  while (right < nums.length) {
    if (nums[right] !== 0) {
      let tmp = nums[right];
      nums[right] = nums[left];
      nums[left] = tmp;
      left++;
    }
    console.log(nums[left]);
    right++;
  }
  return nums;
};
console.log(moveZeroes([0, 1, 0, 3, 12])); // Output: [1,3,12,0,0]
[1, 3, 0, 0, 12];
