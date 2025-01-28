# Pattern Generator

Pattern Generator is a Python-based tool designed to generate and display a variety of patterns, including geometric and numeric shapes. These patterns can be highly customizable and are generated dynamically using pattern definitions written in a declarative syntax.

## Features

- **Dynamic Pattern Generation**: Easily define and render patterns like rectangles, pyramids, diamonds, and more.
- **Custom Syntax**: A flexible syntax for defining patterns, supporting loops, conditions, and calculations.
- **Formatted Output**: Displays patterns in an aesthetically pleasing format using ASCII art.
- **Extensibility**: Add new patterns with minimal effort.

## How It Works

The project leverages Python’s capabilities to process pattern definitions and display them in a user-friendly format. It includes:

1. A **pattern definition file** ([patterns.pg](https://github.com/ajratnam/PatternGenerator/blob/main/patterns.pg)) to define patterns using the custom syntax.
2. A **pattern generator engine** ([pattern_generator.py](https://github.com/ajratnam/PatternGenerator/blob/main/pattern_generator.py)) to parse and render the patterns.
3. Example usage through a script ([script.py](https://github.com/ajratnam/PatternGenerator/blob/main/script.py)), which demonstrates the generation of predefined patterns.

## Pattern Syntax

Patterns are defined using a simple syntax that supports loops, dynamic evaluations, and conditions. Below is an example:

```plaintext
[* ,5],3
```

This generates a solid rectangle with 3 rows, each containing 5 stars (`*`).

### Syntax Details

- **`[symbol, count]`**: Defines the symbol and how many times it should repeat in a single line.
- **`range..step`**: Creates a loop from `start` to `end` with a defined step.
- **`{expression}`**: Embeds dynamic expressions for calculations.
- **Stack-based variables (`!`)**: Use `!` to represent the current loop index or `!!` to refer to the outer loop index.
- **`low..high..low`** allows multiple ranges in a single loop.
- **`low..high$..low`** runs the same range as above, but in the second loop it does not repeat high again.
## Sample Patterns

Here are some of the sample patterns provided:

1. **Solid Rectangle**  
   ```
   * * * * *
   * * * * *
   * * * * *
   ```

2. **Hollow Rectangle**  
   ```
   * * * * *
   *       *
   * * * * *
   ```

3. **Half Pyramid**  
   ```
   *
   * *
   * * *
   ```

4. **Inverted Half Pyramid**  
   ```
   * * * *
   * * *
   * *
   *
   ```

5. **Solid Diamond**  
   ```
       *
      * *
     * * *
      * *
       *
   ```

*(For a full list of patterns, refer to the file [output.txt](https://github.com/ajratnam/PatternGenerator/blob/main/output.txt) which has the output for the patterns in [pattern.pg](https://github.com/ajratnam/PatternGenerator/blob/main/patterns.pg))*

## Setup

### Prerequisites

- Python 3.12 or above
- No additional external libraries are required.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ajratnam/PatternGenerator.git
   cd PatternGenerator
   ```

2. Ensure Python is installed and accessible from your terminal.

### Usage

1. Run the `pattern_generator.py` script with a pattern definition file:
   ```bash
   python pattern_generator.py patterns.pg
   ```

2. Or use the `script.py` for predefined examples:
   ```bash
   python script.py
   ```

3. The output will display formatted patterns in the terminal.

### Example Output

```plaintext
╭────────────────────────────────────────╮
│           1. Solid Rectangle           │
├────────────────────────────────────────┤
│               * * * * *                │
│               * * * * *                │
│               * * * * *                │
╰────────────────────────────────────────╯
...
╭────────────────────────────────────────╮
│           16. Hollow Diamond           │
├────────────────────────────────────────┤
│                   *                    │
│                  * *                   │
│                 *   *                  │
│                *     *                 │
│               *       *                │
│               *       *                │
│                *     *                 │
│                 *   *                  │
│                  * *                   │
│                   *                    │
╰────────────────────────────────────────╯
```

## Customization

### Adding New Patterns

To add a new pattern:
1. Define it in the `patterns.pg` file or `script.py` as a dictionary entry:
   ```python
   "Custom Pattern": "[symbol ,count],rows",
   ```
2. The generator will automatically render it during execution.

### Adjusting Output Styles

- Modify `justify_size` or `auto_index` in the `ComplexPatternGenerator` class for custom formatting.

## Contributing

Contributions are welcome! If you have suggestions for new patterns, optimizations, or features:
1. Fork the repository.
2. Create a new branch:  
   ```bash
   git checkout -b feature-name
   ```
3. Commit and push your changes.
4. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/ajratnam/PatternGenerator/blob/main/LICENSE) file for details.