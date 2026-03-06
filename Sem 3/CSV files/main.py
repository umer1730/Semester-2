from load_csv import read_csv
from process_csv import filter_by_value,compute_average,random_sample
from output import write_csv
import config


def main():
    header,data = read_csv(config.INPUT_FILE)
    sampled = random_sample(data, config.SAMPLE_FRACTION, seed = config.RANDOM_SEED)
    filtered = filter_by_value(sampled,data,col_index=config.PRICE_COL,threshold=config.THRESHOLD)
    avg = compute_average(filtered, col_index=config.PRICE_COL)

    print(f"Average of filtered: {avg}")
    write_csv(config.OUTPUT_FILE, filtered,header)

if __name__ == "__main__":
    main()