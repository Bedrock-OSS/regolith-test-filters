This project provides remote filters for testing
[Regolith](https://github.com/Bedrock-OSS/regolith). If you're looking for
standard Regolith filters please visit [regolith-filters](https://github.com/Bedrock-OSS/regolith-filters)
repository.

## gh-release-filter
A filter for testing downloads of filters from GitHub releases. The
`gh-release-filter-1.0.0` release has a `gh-release-filter-1.0.0.zip` file with
a copy of the filter that writes `Downloaded with github release` instead of
`Downloaded with git`. The `gh-release-filter-1.0.1` tag has no release, so
Regolith has to fall back to git.
