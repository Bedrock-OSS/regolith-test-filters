from pathlib import Path

# The ZIP files attached to the GitHub releases of this filter contain a copy
# of this script with SOURCE set to "github release". Regolith downloads the
# release files when GitHub CLI is available and falls back to git otherwise,
# so the output tells the tests which download method was used.
SOURCE = "git"

def main():
    with Path("BP/gh_release_filter.txt").open("w") as f:
        f.write(f"Downloaded with {SOURCE}")

if __name__ == '__main__':
    main()
