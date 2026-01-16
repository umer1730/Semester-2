class InvalidScoreError(Exception):
    pass

def process_scores(filename):
    total = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                score = int(line.strip())
                if score < 0 or score > 100:
                    raise InvalidScoreError(f"Score {score} is out of bounds!")
                total += score
        print(f"Total Score: {total}")
        
    except FileNotFoundError:
        print("Error: The file 'scores.txt' does not exist.")
    except ValueError:
        print("Error: The file contains non-numeric data.")
    except InvalidScoreError as e:
        print(f"Validation Error: {e}")
    finally:
        print("File processing attempt finished.")


with open("score.txt", "w") as f:
    f.write("90\n85\n-5\n70") 
process_scores("score.txt")