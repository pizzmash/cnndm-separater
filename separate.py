import sys
import os
import hashlib
import shtil


num_expected_cnn_stories = 92579
num_expected_dm_stories = 219506

all_train_urls = "url_lists/all_train.txt"
all_val_urls = "url_lists/all_val.txt"
all_test_urls = "url_lists/all_test.txt"

separated_train_dir = "train"
separated_val_dir = "val"
separated_test_dir = "test"


def read_text_file(text_file):
  lines = []
  with open(text_file, "r") as f:
    for line in f:
      lines.append(line.strip())
  return lines


def hashhex(s):
  """Returns a heximal formated SHA1 hash of the input string."""
  h = hashlib.sha1()
  h.update(s)
  return h.hexdigest()


def get_url_hashes(url_list):
  return [hashhex(url) for url in url_list]


def separate(url_file, cnn_stories_dir, dm_stories_dir, out_dir):
  url_list = read_text_file(url_file)
  url_hashes = get_url_hashes(url_list)
  story_fnames = [s+".story" for s in url_hashes]
  num_stories = len(story_fnames)

  for idx, s in enumerate(story_fnames):
    if idx % 1000 == 0:
      print("Copying story {} of {}; {:.2f} percent done".format(idx, num_stories, float(idx)*100.0/float(num_stories)))

    if os.path.isfile(os.path.join(cnn_stories_dir, s)):
      shutil.copy(os.path.join(cnn_stories_dir, s), os.path.join(out_dir, s))
    elif os.path.isfile(os.path.join(dm_stories_dir, s)):
      shutil.copy(os.path.join(dm_stories_dir, s), os.path.join(out_dir, s))
    else:
      print("Error: Couldn't find story file {} in either story directories {} and {}.".format(s, cnn_stories_dir, dm_stories_dir))
      print("Checking that the stories directories {} and {} contain correct number of files...".format(cnn_stories_dir, dm_stories_dir))
      check_num_stories(cnn_stories_dir, num_expected_cnn_stories)
      check_num_stories(dm_stories_dir, num_expected_dm_stories)
      raise Exception("Stories directories {} and {} contain correct number of files but story file %s found in neither.".format(cnn_stories_dir, dm_stories_dir, s))

  print("Finished copying.")


def check_num_stories(stories_dir, num_expected):
  num_stories = len(os.listdir(stories_dir))
  if num_stories != num_expected:
    raise Exception("stories directory {} contains {} files but should contain {}".format(stories_dir, num_stories, num_expected))


def main():
  if len(sys.argv) != 3:
    print("USAGE: python {} <cnn_stories_dir> <dailymail_stories_dir>".format(sys.argv[0]))
    sys.exit()
  cnn_stories_dir = sys.argv[1]
  dm_stories_dir = sys.argv[2]

  # Check the stories directories contain the correct number of .story files
  check_num_stories(cnn_stories_dir, num_expected_cnn_stories)
  check_num_stories(dm_stories_dir, num_expected_dm_stories)

  # Create some new directories
  if not os.path.exists(separated_train_dir):
    os.makedirs(separated_train_dir)
  if not os.path.exists(separated_val_dir):
    os.makedirs(separated_val_dir)
  if not os.path.exists(separated_test_dir):
    os.makedirs(separated_test_dir)

  # separate
  separate(all_train_urls, cnn_stories_dir, dm_stories_dir, separated_train_dir)
  separate(all_val_urls, cnn_stories_dir, dm_stories_dir, separated_val_dir)
  separate(all_test_urls, cnn_stories_dir, dm_stories_dir, separated_test_dir)


if __name__ == '__main__':
  main()

