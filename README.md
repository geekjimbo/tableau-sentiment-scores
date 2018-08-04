# Tableau Sentiment Analysis Sample
`By: Ing. Jimmy Figueroa`

This sample contains sentiment scores of opinions/tweets for Elon Mush and Hotel recommendation systems.
The `sentiment_scores` are calculated both from within Tableau Workbook, by leveraging Tableau to `TabPy` integration (a.k.a Python), and also from outside Tableau by leveraging `knime` workflows.

## Pre-requisites
* have `TabPy` installed and server running in your local environment
* have `knime` installed and python configured from within `knime`
* have all necessary python packages used by the `python_snipet.py` file, installed in your local environment
* connect your `tableau desktop` to your `TabPy` server 

## Elon Musk
Idea is to have `tableau` calculate the scores for `elon musk tweets` text. 
Open the `*.twb` tableau workbook and locate the calculated field called `sentiment_scores` to lookup the python code

Sample code to calculate `sentiment_scores` for Elon Musk's tweets as follows:

      SCRIPT_REAL("
      from nltk.sentiment.vader import SentimentIntensityAnalyzer
      sentences = _arg1
      scores = []
      analyzer = SentimentIntensityAnalyzer()
      for sentence in sentences:
          vs = analyzer.polarity_scores(sentence)
              scores.append(vs['compound'])
              return scores
              ", ATTR([TweetText]))

## Hotel Recommendations
Idea is to `first` calculate the `sentiment_scores` from within `tableau`.
This yields various issues:
  * 1st is too slow to have Tableau calculate each individual score from the 34K observations
  * 2nd the file have been loaded in `tableau` as a `utf-8` encoding, which results in errors when the characters are not readable in that encoding
  * 3rd we can't use the calculated `sentiment_scores` in tableau to actually build things like distributions or derive other fields from it

One possible way to address this problem is to take the calculation of `sentiment_scores` out of Tableau and into the `ETL` process.
We have several ways to accomplish this:
  * Write a python program -- or use any other programming language (i.e. R) for that matter
  * Leverage the *new* `TableauPrep` tool to write a transformation workflow
  * Leverage `Knime` to write a transformation workflow

`Write a Python Program` is always my preffered choice. But for the purpose of adventure, let's not take that path.

`TableauPrep` is a limited option, mainly because it lacks integration with Python, or any other language.
Sadly, Tableau folks did integrate `Tableau Desktop` with `python` and `R` .. but not their new tool `Tableau Prep`.
The other problem `TableauPrep` has is the fact that it won't work in `Big Data` use cases.

For all practical matters, whatever you can do in `TableuPrep`, you can do much more and better with `Knime`.
`Knime is an Open Source tool` specially designed for `Data Analysts`, it's free, it's cool, it's well conceived, it has lots
of functionally that `TableauPrep` does not offer, and you can run `workflows` from the `tool` of from the `command line` as well.

You can access the `knime workflow` for the purposes of calculating the `sentiment_scores` of this sample
in the follow link `git@github.com:geekjimbo/knime-workflow-sentiment-scores.git`

Enjoy!

`Ing. Jimmy Figueroa A.`
