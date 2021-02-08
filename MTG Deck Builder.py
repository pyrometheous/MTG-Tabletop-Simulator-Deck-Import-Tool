import scrython
import time
import wx
import wx.adv
import wx.stc
import sys
import os
from wx.lib.embeddedimage import PyEmbeddedImage
import shutil
import requests
from PIL import Image

ico_img = "iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAYAAAD0eNT6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAACAASURBVHic7d15mB1Vgffxb3WSCsgO4goKjawWCKQDiKPjLuq44Dij4ziuSOE24gKtwwiK42iLgCMyWoji9uroO47LqCwq6quCkk5YLDaRFhR3ERGEpJJ0vX/cCyaQpfveqnuq7v1+nqcfnge6zvklQM6v61adE5VliSRJGi1joQNIkqTBswBIkjSCLACSJI0gC4AkSSPIAiBJ0giyAEiSNIIsAJIkjSALgCRJI8gCIEmapygKnUD9i9wJUJK0KTedfviOq1YXr2a2nIii6GBgpxIuj4iWR2Ozn939uOXfDZ1R82cBkCRt1My7lj6NsfJs4IEb+ZYyKjlj0eL4zbu8/qI7B5lN/bEASJI26KdTS15dEn1gjt++YuXKlY/c76S8qDWUKuMzAJKke5k55aA9S6JT5nHJwYsXLz6xtkCqnAVAknRvaxd8BNhyPpdEUTT50/cuOaCmRKqYBUBDqcjTsSJPF4TOIbXRNe86dCciHt3DpQuZHXtG5YFUi4WhA0hVKPL0ScBfAfsC+wB7AmNFnl4HXA1cA1wUJ9m54VJK7bAoWrMUenzTryyXVptGdbEAqNWKPH0C8A7gkRv5lod3v+76/mXAW+MkO38A8aRWGhsbW9LrA+IlLKk4jmpiAVArFXn6cOADwGPneelS4LwiT78HvCZOssurzia1XUm5TR+X93OtBshnANQ6RZ7uAXyT+S/+6/or4JtFnu5bSShJahkLgFqlyNP7AxcA969guJ2AC4o83bWCsSSpVSwAao0iT7cFzgXGKxx2Fzol4L4VjilJjWcBUJucCBxUw7j7AO+qYVxJaiwLgFqhyNMYeHGNUzy/yNOtaxxfkhrFAqC2OBKo8zb91sDzahxfkhrFAqC2OHoAcxw1gDkkqREsAGq87mt/jxvAVIcVebrfAOaRpOAsAGqDx9PzvqTz9oQBzSNJQVkA1AaD3Fp0YoBzSVIwFgC1wSAXZQuApJFgAVCjdV//23+AU+5T5OlWA5xPkoKwAKjp9gfiAc43Bhw8wPkkKQgLgJouxC15jzOVNPQsAGq6EAXA5wAkDT0LgJouxE/jFgBJQ88CoMYq8nQxkASYeq/uyYOSNLQsAGqyRwCLAswb4YOAkoacBUBNFvJhPD8GkDTULABqspCLsAVAIysqWd3H5f1cqwGyAKjJLABSALNEV/Z6bVmWPV+rwbIAqJGKPN0SCHky3x5Fnu4QcH4pmHKsXNbzxVHU+7UaKAuAmuoRwMLAGdwQSCPpYcdNX1/CL3u5diyKvlt1HtXDAqCmasIt+CZkkIIoiV4132uiKDpv9+OXfbmOPKqeBUBN1YSfvi0AGlkPm1z2pQg+MY9LblnI2pfXFkiVswCoqZqw+DYhgxTMojg+JoIzgHIz3/qjsbGxx+96/IqePjZQGFFZbu7fqzRYRZ7eB/gTsCB0FmDnOMl+HzqEFNL175l43BjRO8uyPAjYYp1/9NOyLD+9atWqk/c7KS9C5VNvQj9kJW3IgTRj8YfOXYDzQoeQQtrj+OlvAYcvP2ti0Xa3sv+Ctdx39SJW7PXGactxi1kA1ERNuvW+BAuABMCSo6dXAytC51A1LABqoiYVgCZl0QiYmZpYROcQrAOALSsefhWQA1eMT06vqnjsOZuZmtiNTrneueKhS2AGWDE+OX1zxWMPHZ8BUOMUeXolYTcBWtdNcZLtGjqEht/M1MQ48EHgsUBc83SrgYuAV49PTg9k576ZqYnFwMnAUcCOA5jyBuDE8cnpTw5grlayAKhRijzdGriVZr2h8oA4yX4TOoSG18zURAqcCmw14KlXAW8DpsYnp2tbDGamJpYAnwT2rWuOTfgi8IrxSZ9XuKcm/SErARxE8/679GMA1WZmauLZwIcY/OIPsBh4F5DWNcHM1MTOwLmEWfwBng18KtDcjda0P2ilJmwAdE8WANViZmpiJzqLf2indD+Xr8MHqf6z/vl6yszUxFGBMzSOBUBN08TFtomZNBzeAtw/dAhga+AdVQ86MzXxKOBvqx63R++dmZrwwfd1WADUNE1cbJuYScPhUaEDrOORLRmzV9sBDw8dokksAGqMIk+3AfYKnWMDHlDk6YNDh9Bw6b7ud2DoHOsYn5ma2K7iMQ+ueLx+LQ0doEksAGqSg4EodIiN8C6AqrYT62+rG1oEPKjiMZtWnHcJHaBJLABqkkNDB9iEJmdTC41PTv8aaNLrpSuB6yoe84qKx+vXZaEDNIkFQE3y5NABNqHJ2dRey0IHWMcV45PTayoes2nbBjfp9zs4C4AaocjTrYBHh86xCQcXeXq/0CE0dL4QOsA6vljDmN8A/lzDuL1YNj45/YvQIZrEAqCmeDz1b3/ajwh4SugQGi7jk9MfpbNIhnYp8N6qBx2fnP458Oaqx+3BKuCloUM0jQVATXFE6ABz0IaMap+XA38IOP+fgZeMT06vrmn8M4ELahp7rk4Y1JkHbWIBUFO0YXF9cpGn/j+jSo1PTv8M2J/OdrmD9l3gEeOT07U9rNc9Y+DpwEl0DiEapN8CR45PTp864HlbwcOAFFyRp3sCPw6dY44OiZPMB4lUi5mpiX+g88DpwXROxKx657pZ4BpgOXAh8PE6DwG6p5mpiUcAL6bz6zsI2LaGaX5J5+HDaeBMDwHaOAuAgivy9LXA+0PnmKMT4ySrfMtU6Z5mpiYWAIsqHnZNDU/692RmaiKicxhRlcrxyelVFY85tCwACq7I068BTw2dY44ujpPs8NAhJKlfFgAFVeTpFnQegNoydJY5WgvsHCfZLaGDSIM0MzWxP1E5Uc5ycBRxX8roMhhbvtXCVRff/02XN+VVP82DJyMptMfQnsUfYAHwJOBzoYNIg3DNuw7dafGC2TOB51FGRHdt1h3xfJjlz2sW3Xj9u5e8bI83L78wZE7Nn080K7Rnhw7QgzZmlubtp+9Zekg8tjYvy/J5G/2miIdGUfSNmamJdw0wmirgRwAKpsjTHYCfA1uFzjJPq4Hd4yRzVzENrV+9feI+d27B5cDD5npNFEXP2v34ZV+uMZYq5B0AhXQM7Vv8ofNk9mtDh5DqtHIL3s08Fn+Asiyzm04/fMeaIqliFgAFUeRpTLsX0bR7foE0dG54++O2KDsFfb4eUKwunl95INXCAqBQXgA8MHSIPmwPvCx0CKkW8W2PoMc9CKJZDqk4jWpiAVAobwwdoALHujWwhtHasd4X8TJiaZVZVB//8NLAFXn6FCAJnaMC48CRoUNIVYsiHtzH5f1cqwGyACiEN4UOUKE3hA4gSb2wAGigijx9BPDE0DkqdHiRp4eFDiFJ82UB0KANw2f/9zSMvyZJQ84CoIEp8vQhwDC+InRkkafzel9akkKzAGiQzqD6402bYAFwZugQkjQfFgANRJGnzwWeGTpHjZ5c5OmLQoeQpLmyAKh2RZ5uT+en/2F3WpGnO4cOIUlzYQHQILwHeEDoEAOwE/C+0CEkaS4sAKpVkaePAY4KnWOAXlDk6VNDh5CkzbEAqDZFni4GzgKi0FkG7ENFnm4dOoQkbYoFQHX6V2Dv0CECeAjwztAhJGlTLACqRZGnCTAZOkdAryny9NDQISRpYywAqlz3hLwPM5zv/M/VGHB2kaej/HsgqcEsAKrDvwPuj9858fD9oUNI0oZYAFSpIk+PZrRv/d/TMUWeHhc6hCTdkwVAlem+/vafoXM00FR3J0RJagwLgCpR5OmBwOfo7Iuv9UXAJ4s8fWToIJJ0FwuA+lbk6S7AVwHffd+4LYAvFXk6HjqIJIEFQH0q8nRb4GvAg0JnaYGdga8Vebpj6CCSZAFQz4o8XQj8N7B/6CwtsjfwhSJP49BBpI0qKfu6Wq1gAVA/MuBJoUO00GOAc0KHkDbhZ31c+/PKUqhWC0MHUPsUeRoB7wZeFjpLi72gyNPfAa+Pk8yfmNQs0ewyyp5/Prykyiiqj3cANC/dA34+BRwfOssQeB3wuSJPtwgdRFrXyjuLK4BVvVxbEi2rOI5qYgHQnHUfXvs68ILQWYbIc4FvFXm6c+gg0l32OykvKDlt3heW3LgmWvzpGiKpBhYAzUmRp3sAFwOPDp1lCB0G/KDI01E8OVENtXLVyrdRcsU8LinLMV669/Hfu622UKqUBUCb1d3A5mJgr9BZhtg4cFGRp48JHUSCzl2ABWPl84Fr5/DtBVH5hj2On/5W3blUHQuANqm7he2FdN5hV712BL5e5KkfsagRHnr88qvjOD4I+A82/nrf5RGzh4wfv/x9A4ymCkRl6QPI2rDuITZTdLay1eCUwFvjJHtn6CDSXW445ZAHlLNrl1JGS8uI+0ZRtJyx2WW7P3SPK/m7z60NnU/zZwHQvRR5uiXwPuDo0FlG3MeA18RJ9ufQQSQNHwuA1lPk6eOAs4CHhc4iAG4A0jjJLggdRNJwsQAIgCJPtwdOAY4KnUUb9Ek6mwbdHDqIpOFgARBFnv4t8AHgAaGzaJN+BxwbJ5nvWUvqmwVghBV5+iA6C/+RobNoXs4FXhkn2Y2hg0hqLwvACOru5X8UnVv+2wWOo97cDvwrcEacZLOhw0hqHwvAiCny9CDgdOCvQ2dRJX5I59mAi0MHkdQuFoAR0P2J/2nAG4HHBY6jelwEnAZ8wTsCkubCAjDEuqfMvQh4PbBP4DgajBk6ezh81P0DJG2KBWAIFXl6P+BV3S+38B1Nt9DZz+GMOMl+ETqMpOaxAAyRIk/3Bd4AvBDwjHkBrAb+CzgtTrLLQoeR1BwWgJYr8jQBjgCeTufBPvft18Z8H/gqndcIL4+TzP/5pRFmAWiZ7o59T6Sz6B8BPDhsIrXUr4HzgfOAC+Ik+0PgPJIGzALQcN0n+JfwlwX/MGBB0FAaNrPAJXTKwHnAMt8kkIafBaBhijzdBjgYmAAOofPang/yaZBuBi4ElgHTwIo4yW4NG0lS1SwAARV5uhVwIJ3F/q6vvfFzfDVLCVxHpwzc9XVpnGS3B00lqS8WgAHpvpN/z8V+H7ydr3aaBa5h/VJwWZxkdwZNJWnOLAA1KPI0Bg5g/cX+4cDCkLmkmq0FrmT9UnBFnGSrgqaStEEWgD4VeboQSFh/sd8fiEPmkhpiNfAj1i8FeZxkq4OmkmQBmI8iTxcA+7L+Yv8I3HRHmo9VwOWsXwquipNsbdBU0oixAGxC9xW8xwPPoLPYHwTcJ2goaTjdCVxKpwx8FfiGryJK9bIAbECRp7sALwFeBuweNo00km4EzgHOiZPsZ6HDSMPIArCOIk93BD4K/A0+nS81wSydrYtfGifZ70KHkYaJBaCryNMHARfQeVpfUrNcCzzZuwFSdcZCB2iCIk8fRuegFBd/qZn2Br5X5Ok+oYNIw2Lk7wAUebornS1P7x86i6TN+j1waJxkM6GDSG3nHQA4CRd/qS3uC/xb6BDSMBjpOwDdW/9X4w59UpuUwIFxkl0ROojUZqN+B+BtuPhLbRPhXQCpbyN7B6D7rv+NWIKkttovTrKrQ4eQ2mqUF79HMNq/fqntDgwdQGqzUV4AfZ1Iare9QgeQ2myUC8C+oQNI6sveoQNIbTbKBcCfHqR22zN0AKnNRrkA/DF0AEl9uTV0AKnNRrkAXBM6gKS+XBs6gNRmo1wAfH1IajcLgNSHUS4A3gGQ2u3HoQNIbTbKBeBS4JehQ0jqyS3ARaFDSG02sgUgTrKVwDtD55DUk6k4yf4UOoTUZiNbALrOprMdsKT2+DVwRugQUtuNdAGIk6wATg6dQ9K8/FucZHeEDiG13UgXgK6P0bkTIKn5PglkoUNIw2BkTwO8pyJPp4DjQ+eQtFHvB46Nk8w/tKQKWADWUeTp8cBU6ByS7uWkOMn8uE6qkAXgHoo8fRxwDPBsIA4cRxplq4EvAx+Kk+wbocNIw8YCsBFFnu4EvBA4CkgCx5FGyVXAR4BPxkn2u9BhpGFlAZiDIk93AybW+VoCbB8ykzQkbgWWA9N3fcVJ9tOwkaTRYAHoQZGnEbAH65eCg4FtQuaSGu52YAXrLPbAT3yoTwrDAlCRbinYm/VLwYHAViFzSYHcSWe77XUX+2vjJJsNmkrS3SwANSrydAGwL+uXgkcAW4TMJVVsFXA56y/2V8VJtjZoKkmbZAEYsCJPF9J5qHDd5wkOwDcO1A6rgR+x/mKfx0m2OmgqSfNmAWiAIk9jYH/Wv1OQAAtD5tLIW0Pnifx1F/sr4iRbFTSVhkKRp4cAT6dzl3QfOg9WX0vnqPYVwKf9b61eFoCGKvJ0C+Ag4AnAEcBhwIKgoTTsZoFLgPOArwOXxkl2Z9hIGjZFnh5I5wyWZ2zmW2/qft85cZKtqT3YCLIAtESRp9sDT6RTBo4AHhw2kYbEr+ks+OcBX4+T7A+B82iIFXk6CbwLiOZx2aXA4+Mk+2M9qUaXBaClijxN+EsZeDQ+Q6C5WQ1cxF8W/ct9DU+DUORpCnyox8u/DzzZUyCrZQEYAkWebkXn7sArgacEjqNm+jZwJnBBnGR/CpxFI6bI0+cA/5f+TqA9F3i6hbU6FoAh070z8AbgBcDiwHEU1hrgc8CpcZKtCB1Go6vI02uBvSoY6olxkn2zgnGEBWBoFXn6AODVdO4K7BQ4jgbrVuAs4P1xkt0UOoxGW5GnfwV8t6LhPhsn2fMrGmvkWQCGXJGnWwIvAY6lmgau5roB+A/gI3GS3RY4iwRAkacfBV5a0XCrgAfHSXZzReONNAvAiOhuVfwM4I3AYwLHUbV+CJwK/I+776lJijxdBNxCtVuivzJOsl4fJtQ63GhmRHQfnPky8OUiT4+k80DYA8OmUp9+DxwbJ9n/CR1E2oiHU/15KIfR+9sEWkc/T2SqpeIk+wKd3bc+DHgLqJ0+Bezr4q+GW1rDmBM1jDmS/AhgxBV5+td0isCeobNoTm4AjomT7PzQQaTNKfI0A46ueNi1wHZxkv254nFHjncARlycZN+hcxjRu+m8NqZmWgucDiQu/mqROn5aX0DnqHX1yTsAult3j+6z6ZxQqOa4AjgqTrJloYNIc1Xk6WLgNmBRDcMfGyfZf9Qw7kjxDoDuFifZZcChwHGAh8CEtwo4AVji4q8WOoB6Fn/wOYBK+BaA1tN9jey9RZ5eCHwF3xQI5bfAM+Mk+2HoIFKP6lykLQAV8A6ANqi7dexhQB46ywi6BjjMxV8tV+civVeRp9vUOP5IsABoo+Ik+xnwKOAbobOMkO8Ah8dJ9tPQQaQ+1VkAxoCDahx/JFgAtEndk+OeCnw0dJYR8Ck6R57eEjqI1I/uFuQPr3kaPwbok88AaLPiJFsDvLzI0xngHUAUONIwekecZCeGDiFV5EA6r+vVyQLQJ+8AaM7iJHsn8EI6T6erGquBl7r4a8gMYnH2deU+WQA0L3GSfRp4EvCH0FmGwK3AU+Mk+1joIFLFBlEA9izydLsBzDO0LACatzjJvkvnRME/hs7SYrcBj4uT7Juhg0g1qOMMgHuKgIMHMM/QsgCoJ3GSXQk8h84tbM3PWuB5cZJdGjqIVLUiT7cG9h7QdD4H0AcLgHoWJ9m3gKNC52ihV8dJdm7oEFJNDmZwa4vPAfTBAqC+xEn2CeBtoXO0yClxkmWhQ0g1GuRP5d4B6IMFQH2Lk+ztwMdD52iB/wYmQ4eQajbIRXmPIk93GOB8Q8UCoKq8AvCBto27GPinOMk8flPDbtA/lfsgYI8sAKpEnGSrgb8FrgydpYGuB54VJ9nK0EGkOnVfy3vYgKf1Y4AeWQBUmTjJbgWeBvwqdJYG+QPwtDjJfhc6iDQASxj8TqEWgB5ZAFSp7gFCzwCK0FkaYBZ4TpxkPw4dRBqQEIuxBaBHFgBVLk6y5cBU6BwN8IE4yb4TOoQ0QCEW492KPN0pwLytZwFQXd5J51z7UfUz4ITQIaRBKfI0Av460PSh5m01C4BqESfZKuBoYFSfej8mTrLbQ4eQBugg4H6B5j4i0LytZgFQbbpnBnw4dI4APu1OfxpBIRdhC0APLACq2/GM1lsBNwPHhg4hBRByEd61yNP9As7fShYA1ar7auBrQ+cYoDf4yp9GTff9/0cGjvHUwPO3jgVAtYuT7PPAl0LnGIALumcjSKPmicDCwBn8GGCeLAAalFcDfwodokZ3AMeEDiEF0oTF99FFnt4ndIg2sQBoIOIk+wXwltA5avTWOMl+GjqEFMhTQgcAFgOPCx2iTSwAGqQMuCF0iBr8EvhA6BBSCEWeTgC7hs7RdWToAG1iAdDAxEm2Fnhf6Bw1+ECcZG59rFHVpLde/rHI051Dh2gLC4AG7SPAH0OHqNCfgQ+FDiGFUOTpLsDzQudYxxbAq0KHaAsLgAaquzteFjpHhc6Jk+yW0CGkQP6Z8E//39OrijzdInSINrAAKIQzgNWhQ1RgluH8SEParCJPt6az3XfT3A/4p9Ah2sACoIHrvhHwmdA5KvClOMmuDx1CCuTlwHahQ2zE67uHE2kTLAAK5dTQASowDL8Gad6KPF1Asx7+u6d9cWfAzbIAKIg4ya4Avh46Rx9+GCfZ90OHkAJ5DrBb6BCb8cbQAZrOAqCQ2vwT9GmhA0ghFHm6EHhr6Bxz8PgiT/86dIgmswAomDjJzgfy0Dl6cAPw+dAhpECOA/YPHWKOzvKNgI2zACi0s0MH6MHHupsaSSOlyNM9gRND55iHvWjH3YogLAAK7dzQAXrQxsxSX7pP1Z9FZ7OdNjmuyNO23LEYKAuAgoqT7MdAmw7RuRmYDh1CCuDlwGNDh+jBIuDsIk9d7+7B3xA1wXmhA8zDBXGSzYYOIQ1SkacPAE4JnaMPh9DZtVDrsACoCdpUANqUVarKGcD2oUP06d+KPH1o6BBNYgFQE1wItOE0vRI4P3QIaZCKPP0H4Lmhc1RgK+Cj3dcYhQVADdA9IOh7oXPMwaVxkv0mdAhpUIo8PRz4aOgcFXo8cGboEE1hAVBTtOHWehsySpUo8nQP4Eu076n/zTm6yNPJ0CGawAKgpmjD4tqGjFLfijzdEfgacN/QWWryriJP/y50iNAsAGqEOMl+BPwidI5NuBW4OHQIqW5Fni4GvkhnE51hFQGfKPL0kaGDhGQBUJM0+QG7b8ZJtiZ0CKlO3c1+Pgo8OnSWAdgC+HL3o46RZAFQk3wrdIBNaHI2qSrvAF4QOsQA3Rf4WpGnO4UOEoIFQE3S5B32mpxN6kuRp2NFnp4OnBA6SwB7Ad8v8nQ8dJBBswCoSX4M3BY6xAasAS4LHUKqQ5Gn9wH+Bzg2dJaA9gZ+UOTpYaGDDJIFQI3R3WL30tA5NuDKOMlWhg4hVa3I0/sD3wGeFTpLA+wMXFjk6d+GDjIoFgA1TRNvtTcxk9SXIk/3A34ITITO0iBbAv+3yNM3hQ4yCBYANU0TF9smZpJ6VuTpE4CLAPfGv7cIOKXI0w8WebogdJg6WQDUNMtDB9gAC4CGQvdhv2OBc4HtQudpuGOAc4s83SV0kLpYANQ01wF/Ch1iHQVwRegQUr+KPN2fzk/9pwOLAsdpiycBVxZ5+qruHglDJSrLMnQGaT1Fnl4IPC50jq7lcZL5Galaq7uz31uB43Hh78f3gVfESXZ16CBV8Q6AmqhJHwN4+1+tVeTpY4DL6bzf7+Lfn0cBlxV5elKRp3HoMFWwAKiJmrToNimLNCdFnm5X5GkGfJvOO+6qRgy8Dbi0e1Ryqy0MHUDagCYtuk3KIm1SkacPBF4LpMCOgeMMs/2A7xV5+jXg1DjJWrlVuM8AqJGKPL0F2D5wjJXANh4CpKYr8vQA4A3AP9D5KVWDdSlwGvDZOMlWhw4zVxYANVKRp98AnhA4xg/jJBuprUHVLkWeHkFn4X9S6CwCOkeavx84K06yP4YOszl+BKCmmiZ8AfD2vxqne2jN0+i8p/7wwHG0vgcDU8Bbizw9B/g8cFFT7wpYANRUTVh8m5BBI657WM9jgSO6X3sGDaS52JrOsxivBW4r8vSbwHnAeXGS3Rg02TosAGqqJrwKaAHQwHU3nNmXvyz4jwEWBw2lfmwDPLv7RZGn19AtA8B34yS7I1QwnwFQYxV5+ntgp0DT3wFsGyfZ2kDza0QUebobnQN57vpaQvgHYDUYa4Gr6PywcdfX5XGSrRrE5BYANVaRp+cDTw40/ffjJPurQHNrSHX3lZ+4x1eokqtmWg3kdMrAsu5f8zqeI/AjADXZNOEKgLf/1ZciT+/P+gv9UuD+QUOpDRYBB3W/XtH9e6uKPL2c9e8UXNXvHUoLgJos5HMAFgDNWZGnO3Hvn+yH9hQ5Ddxi4JDu113uLPL0UtYvBdfGSTY710EtAGqykIuwBUAbVeTpUuDx/GWx3y1oII2iLYHDu193ub3I0xV0/vy6BPhqnGS3b2wAnwFQoxV5+ltg5wFPexuw/XyatIZfkac7A/8EvAzfv1c73A78F/CROMl+cM9/6GFAaroQP4mvcPHXuoo8fSFwE3AqLv5qj62Bo4CLizz9SpGnW677Dy0AaroQzwF4+193K/L0tcAncI99tdvTga8XeXr3K6YWADVdiMXYAiAAijz9Zzp7u0ehs0gVeBTwrSJPY7AAqPksAAqiyNMdgXeEziFV7EC6rxdaANRocZL9AvjNAKf8I3D9AOdTcx0HbBs6hFSDE4o83dICoDYY5E/ky+Mk89WYEVfk6V2HuUjD6IHASywAaoNBFgBv/ws6T/pvFTqEVKNDLABqg2VDOpeaa9/QAaSa7WsBUBt8A7h5APPcRueITmmf0AGkmu1jAVDjdY/G/OQApvqvOMn+PIB51HzBzmiXBuQOC4Da4sMDmOPsAcyhdrg6dACpZldbANQKcZJdBVxU4xR5nGSX1Di+2uWa0AGkml1jAVCbnFLj2O+tcWy1zzXAz0OHkGr0dQuAWiNOsi8Cb65h6H+Pk+zjNYyrloqTbDXuAqjhtTxOsi9aANQqcZJNAadXOORZcZKdUOF4Gh7nAD8JHUKqwQngVsBqpzcCn6pgNDEo3gAAHTxJREFUnP8GXlnBOBpCcZKtAV5K5/VQaVh8ME6y8wGisnTXU7VTkafPAk4GDpjnpVcCJwH/47a/2pwiT5fQ2R/ivqGzSH3693XveFoA1GpFnkbA3wMnAvtt5tuvpfO57mfiJJutO5uGR5GnewMfBw4NnUXqwe+Bt8dJ9oF1/6YFQEOjyNPtgb2Avbt/HQN+TGfhvzZOslsCxtMQKPJ0fzpHqb4Q2CFwHGlTSuBbdPZQ+Z84yYp7foMFQJLmqcjTmM656hPrfO0HLAiZSyPtN3QOM1ve/euyOMl+vakLLACSVIEiT7dk/VKwhM6hQj5srar9jr8s9NN0Xuu7ab6DWAAkqSZFnm4FHESnDNxVDO76eEqai5v5y2K/HJiOk+xnVQxsAZCkASrydBs6pWDdjw8eBkQhc6kRbqGzyN/9032cZDfUNZkFQJICK/J0O+Bg/lIIHgnsGjSU6nYn8APWv41//SADWAAkqYGKPN0POKL79RhgcdhEqsA1dPaUOA/4TpxkK0OGsQBIUsMVeXof4LH8pRDsGTSQ5uo24Jt0F/04yW4MnGc9FgBJapkiTx9GZxvro4BtA8fRvX2DzpklX+8eLNVIFgBJaqkiT7elUwJeBzwkcJxRtxr4DHBanGSXhw4zFxYASWq5Ik8XAs+lc1DWROA4o+YWIAPOiJPsl6HDzIcFQJKGSJGnjwEmgaeFzjLkbgKmgHPiJPtz6DC9sABI0hAq8vRI4APAg0JnGTKzwH8C/xInWauPirYASNKQ6u4vMAUcjRsNVeFK4BVxkl0cOkgVLACSNOSKPH00nVPh9g6dpaUK4J3Auzd0ql5bWQAkaQQUeboY+Fc6zwcsChynTb5P56f+q0MHqZoFQJJGSJGnBwBfAnYLHKXpZoE3A++Nk2woF0oLgCSNmCJP7wf8L3BI6CwNdSfwj3GSfSF0kDp5JKUkjZg4yX5LZ2vhoV7gevRb4LHDvviDBUCSRlKcZHfS2TzotNBZGuRq4NA4yS4JHWQQ/AhAkkZckaevAt4PLAidJaBvAc+Jk+yPoYMMigVAkkSRp08HPgtsFTpLAJ8AjmrywT11sABIkgAo8vSpdB4OHKU7Af8N/P2wPum/KT4DIEkCIE6yc4HXhM4xQD8AXjSKiz9YACRJ64iT7EPAe0PnGIAZ4JndhyFHkgVAknRPxwOfDx2iRrcAT4uT7Hehg4TkMwCSpHsp8nRL4ELgsNBZKlYAT46T7Duhg4TmHQBJ0r10b40/k86t8mHychf/DguAJGmDurfInwmsCp2lIqfGSfap0CGawgIgSdqoOMmupHMUbttdD7w1dIgmsQBIkjbn3cCVoUP06ehRfuJ/QywAkqRN6u6QdxSdI3Lb6Jw4yS4MHaJpLACSpM2Kk+wHwJmhc/TgN8AbQ4doIguAJGmu/gX4eegQ8/S6OMluCR2iiSwAkqQ5iZPsduCVoXPMw1fiJPts6BBNZQGQJM1ZnGRfBb4QOsccrAJeFTpEk1kAJEnz9a7QAebg/8RJ1raPKwbKAiBJmpc4yZYB3w2dYzNOCx2g6SwAkqRenBo6wCac193ASJtgAZAk9eJ/getCh9iIJpeTxrAASJLmLU6yWeB9oXNswBVxkn0jdIg2sABIknr1MeDm0CHuwc/+58gCIEnqSZxkdwAfCp1jHb8CPhM6RFtYACRJ/fggUIYO0fXhOMmK0CHawgIgSepZnGS/AC4LnaPrq6EDtIkFQJLUr/NCB6DzLMJ06BBtYgGQJPWrCQXggu6bCZojC4AkqV8XAX8KnKEJJaRVLACSpL7ESbYG+GbACCVwfsD5W8kCIEmqQsifwC+Lk+w3AedvJQuAJKkKIQuAt/97YAGQJPUtTrKfAVcHmt4C0AMLgCSpKhcFmHMNcEmAeVvPAiBJqkqI9/CvjJNsZYB5W88CIEmqSogC4OY/PVoYOsBczUxNLAJeDhwOLAF2BX4ELAe+Mj45fUHAeJIkuAIogHiAcy4f4FxDJSrLppzhsHEzUxMHAh8HDtjEt30CeN345PQfB5NKknRPRZ4uAyYGOOUhcZItG+B8Q6PxHwHMTE08lc4DHpta/AFeBFw+MzWxU/2pJEkbMchb8qvp3HVQDxpdAGamJnYAzgYWzfGShwBn1JdIkrQZgywAP4qTbNUA5xsqjS4AwHuBB83zmn+YmZp4Rh1hJEmbNcgC4Of/fWh6ATiyx+ueU2kKSdJcXQkM6rU83wDoQ2MLwMzUxDiwQ4+XL6kyiyRpbroHA102oOksAH1obAEADuzj2n1npiYWV5ZEkjQfg1iYCzqvgqtHTS4A2/Zx7UJgy6qCSJLmZRAF4Io4yVYPYJ6h1eQCIElqp0EUAG//98kCIEmq2tXAn2uewwLQJwuAJKlScZLNAitqnsYC0CcLgCSpDnUu0CvpvG6oPlgAJEl1qLMAXN593VB9sABIkupQZwHw9n8FLACSpDpcB/ypprHdArgCFgBJUuXiJCupb6H2DkAFLACSpLrUsVDfAVxVw7gjxwIgSapLHQXgsjjJ1tYw7sixAEiS6lJHAfDz/4pYACRJtYiTbAb4ecXDfrvi8UaWBUCSVKePVzjW74CvVDjeSLMASJLqdA5QVjTWx+MkKyoaa+RZACRJtel+DPDtioY7u6JxhAVAklS/V9K5fd+Pf4mT7NoqwqjDAiBJqlV34T6C3ncGPDVOsndVGElYACRJAxAn2Qrgb4Ab53HZauCUOMneVE+q0WYBkCQNRJxk3wX2Al4N/HIT3zoLfBLYJ06y4weRbRQtDB1gE/rd6cmdoiSpYbpP8f9nkacfBQ4C9gX2AbYHrgWuoXPc703hUo6GJheAa/q49pfjk9O3VZZEklSpOMlWAhd3vxRAkwvAFXQ+/1nUw7VuFamRUuTpfYBx4DdxkvX7tLWkEdDYAjA+Ob1qZmpiBXBoD5dfVHUeqWmKPN0GOBZ4KbAbEHX//s3A+cDb4yT7cbCAkhqt6Q8BHsv8P8u/Dnh/DVmkxijy9JnAT4GTgd3pLv5dOwEvAK4q8vTUAPEktUCjC8D45PQPgFPmccks8JLxyek7aookBVfk6WOBz9FZ6DdlAfCGIk+nag8lqXUaXQC6TgT+DVizme/7NfCs8clpb/9raBV5ujPwZWDxPC47vsjT59UUSVJLNb4AjE9Orx6fnH4rcBjw/4BV9/iWm+kcNvHw8clpT4nSsHsxsE0P17226iCS2i0qy6oOaRqMmamJRcD+wEOBy8cnp2cCR5IGpsjTa4C9e7x8vzjJrq4yj6T2al0BkEZVkaf7AVf2McQJcZL9e1V5JLXbRl8DvO7dh4wvGFt7YDnLtlVOODY2tracja6Z3eqWKx722uvueTt/YG46/fAdi9UrDyoZ24XZMtr8FXM0FpVjRL9ctGjR8l1ef9EfKhtXgonA10saIusVgJ+9+4Ad1kSL3gvRkQsidqCMiKpbGgEoyxKikrE7tls9MzWxYiwqj93t+OU/qHaWjYmin04d/KqS6E3AbjDWeXeqyl9kCSUlRVEwMzVxQxRFp+5+/PSZ4K0W9W1J4OslDZG7PwK4fmrpU6E8O4IHDTjDWuCUW3bgxCVHT6+ua5KfvOewXcbKtR+D8gl1zbExEXybhbMv2f2NK+ZzCpa0niJPvwc8qs9h7udOgZKg+xbADacccmBE+aUAiz903lV+8463cGJdE3z77Y9buKBc8+UQiz9ACY8t14x99Sdn7DmfV7ekuxV5ugA4sIKhDq5gDElDYGz5WROLZtfOfpze9tyvTAlvvv7dS2q5RfmQLf90Qtk5dSqkh4/dsd3bAmdQe+0DbFXBOD4HIAmAsR3+wMuJOCB0EGBhFI2dVvWg17/3EfejjE6oetweHfeT9xy2S+gQaqWlDRtHUsuNlZSHhw7xF+Why8+aqPROxNjahYcS+O7GOhaMsfqQ0CHUSk+uaJzHFXna2EPAJA3OWBRFTXoyePF2t7J/tUNGjVpwy3KsSb/faoEiT8eorgBsCzSo9EsKZQzYNXSIdUVry4dWPORDKh6vP+Vso36/1QpL2fzBP/Px1ArHktRSY1D+KHSIdc2y4PIqxyuh0vEq0Kjfb7XCEQ0fT1ILjUVEy0OHuEsEN+/55ksq3ds/GiuXVTleBRrz+63WqPon9gOLPH1gxWNKapkxShpzgl5J9OWqx1y0cPE08Iuqx+3Rb1etWnVJ6BBqjyJPd6GeJ/efXcOYklpkbPc3T18QwSdCBwF+HceL3lT1oLu8/qI7S6JXVD1uL8qyPGa/k/LbQ+dQq/wz9Rzb/boiTyve6FtSm4wBRIvXvg74WcAcs4yVr6jr8Jw9JpedW8KH6xh7riL4xB5vXv6FkBnULkWebgMcXdPwewN/U9PYklpgDGC3Yy/9YzG74GAiPhMgw3UlY48eP255rR9F7DG5PC07P03dUec8G3AnZfSG3Vcuf+mA51X7HQVsV+P4ld9xk9Qedx8GdJefTi15Rkn0HDonh+3LJo4M7lUJv+w8fFhetOVK3v/Ak6YHtijPnHLQnswufBVwMJQHAdvUMM3tlFxKFC1nduyD42/54Y9rmENDrLtZz0+Aql+LvaelcZJN1zyHpAa6VwFY10/O2HPxwrVbb1nlhKuKrdbuffz3bqtyzN5F0czUkm3HFq+t7LPQ2VULyvGVy2/jpHK2qjE1eoo8fT4M5I7cZ+Mke/4A5pHUMJssAJIGr8jT+wBXArsNYLoSeEycZN8bwFySGqRVe4LPTE3cDziUzmtRD6Wzyc8yYHp8cvrOkNmkCp3MYBZ/gAg4q8jTA+MkKwY0p6QGaMUdgJmpiYXACd2vDR3s8wvgFeOT0+cONJhUsSJPDwYuARYMeOqT4iQ7ecBzSgqo8QVgZmpiF+DLwEFz+PYPA+n45HSzf1HSBhR5uoDO4n9wgOlXAQfGSXZNgLklBVDHBiOVmZmaiICPMbfFH+AVwGtqCyTV61jCLP4Ai4HMzYGk0dHoAgC8CnjCPK9598zUxJ51hJHqUuTpY4F/DxzjMcBU4AySBqTpBaCXjUruQ6c4SK1Q5Om+wBeAOHQW4LgiT48JHUJS/RpbAGamJnak9yehl1QYRapNkaf3B74GbB86yzo+UOTp00KHkFSvxhYA+lvED5qZmmjyr026633//2Vwr/zN1QLgs0WezvXZG0kt1ORF8kF9XLs19WzxK1WiyNOtgM9Tz1G/Vdga+GqRp0noIJLq0eQC0O/TyD7NrEYq8vRBwP8DjgidZTMeCHy/yNMnhw4iqXpNLgDS0Cny9ADgh4R73W++tqVzJ6CuY4klBWIBkAakyNMjgO8Bu4TOMk8L6ewRMOU+AdLwsABINSvydHGRpycDX6Hdz6YcD3ytyNOHhA4iqX8WAKlGRZ4+CrgUeCuD39+/DkcAVxZ5+poiT/3zQ2ox/weWalDk6TZFnn4A+C6wb+g8FdsaOAP4bncTI0kt1KrjgKWmK/J0MfCPwNuAXcOmqd3hwGVFnr4P+I84yX4ZOpCkubMASBUo8nRn4JV0tqG+f+A4gxTTeTbg9UWefgY4PU6yywJnkjQHFgCpD0We7g+8FvgnYIvAcUJaBLwIeFGRpxcCpwPnxUm2JmwsSRtjAZDmocjTbYDH03kY7giat41vEzy++/WnIk+/CZxHpwz8LGwsSeuyAEibUOTpDnTOpTgEeBLwKDo/7WrztgWO7H5R5OlVwPnAxcCyOMluCBdNkgVA6irydAGdB9sOASbo7NO/R9BQw2W/7tfrAYo8vRmYBpZ1//qdOMn+GC6eNFosABp5RZ7uDrwCeDH9HUKl+dkJeEr3C2BlkaefB86Ok+zbwVJJI8J9ADTSijx9PHA58BZc/EPbgs4rlN8q8vSdocNIw84CoJFV5OnfAF+j3dvzDqt/KfL0zNAhpGFmAdBIKvJ0S+AsYHHoLNqoVxV5+tjQIaRhZQHQqHoNnfPu1Wx+FCDVxAKgUfV3oQNoTg4v8tRnM6QaWAA0qvYKHUBz5r8rqQZNLgBl4Os1pIo83RbYLnQOzdlDQgeQhlGTC0A/J4vdDtxWVRANlzjJ/kTnvxG1g6cMSjVocgFY3se1l45PTs9WlkTD6LrQATRnPw4dQBpGjS0A45PTfwBu6PHyfsqDRsNXQgfQnFwB/Dx0CGkYNbYAdJ3awzV3Ah+sOoiGzmmA+84334lxkvk8j1SDpheAM4Fvz/OaE8Ynp71lqE3qHjrzRnxYtMm+FCfZl0KHkIZVowvA+OR0CbwEuHKOl3wC+I/aAmmoxEn2UTp7z68OnUX3cg7w3NAhpGEWlWXzfwCamZpYDLwNOA5YsIFv+S1wzPjk9BcGmUvDocjTg+nsDPj3wFaB44yyEriQzmmA/xU6jDTsWlEA7jIzNbELnbPalwC7Aj+i88DfJeOT077Wpb4Uebo18FQ6/41N0PnvzIOC6rOGzt29ZcA0cEGcZD8NG0kaHa0qANIgFXkaAXvTKQOHAE8C9gkaqt1+D3wduJjOon9ZnGQrw0aSRpcFQJqHIk8fChzR/XoC3iHYlLXAJcB5wLnA8jjJ3J9DaggLgNSjIk8XAY8FXgv8DRAFDdQcVwLvAz4fJ9ktocNI2jALgFSBIk/3Ao4FXgzcJ3CcUC4ATouT7PzQQSRtngVAqlCRpzsCx9B5Y2X7wHEGoQQ+CZwSJ1keOozqccMphzygnF27FKJDypIdIVpOVC4bHx+/ir/73NrQ+dQbC4BUgyJPHwB8APjb0FlqdC1wVJxk3wsdRPW46fTDtyyK4l3AP7Phj7guj5h98e6TKy4fcDRVwAIg1ajI0yPp7Gj5wNBZKrQaeA/wjjjJVoUOo3rc+J4l+64toy/QeRNmUwqicnL8+OXvG0QuVccCINWsyNPtgFOAV4TOUoFp4OVxkl0ROojqc9Xbk3iLxVssI+KAOV5SlhFP2OP46W/VGkyVavRWwNIwiJPs1jjJjqbzgGCbtx3+JPAoF//ht8XiLd42j8UfIIpmOefa9/yVr8W2iAVAGpA4yT4BPIV2nkJ4cpxkL4qTrAgdRPW66u1JTMQb5n1hxEMXlqteUEMk1cQCIA1QnGTfAh4F3Bg6yxytBl4SJ9lJoYNoMLbYMj4AWNzLtRHl0orjqEYWAGnA4iS7CjiUzjkWTfYn4Ig4yT4eOogGqBzrZxE/pLIcqp0FQAogTrLf0NlO+Cehs2zEGuC5cZJdGDqIBu4hfVy7a2UpVDsLgBRInGS/B54G3Bw6ywakcZJ9PXQIBRD1taW122G3iAVACihOsuuAZwNNep/+nXGSfTR0CEn1sgBIgXV30nsxnW11Q/s08NbQISTVzwIgNUCcZJ+ls1lQSD8CXhonWROKiKSaWQCk5jiJcA8FztLZ19/3/KURYQGQGiJOspXA0YGmPyNOsksCzS0pAAuA1CDdjYIG/QDez4B/HfCckgKzAEjN8ybgNwOc75Vxkt0+wPkkNYAFQGqYOMluYXA/kX81TrKvDWguSQ1iAZCa6ZMM5i5A6DcPJAViAZAaKE6yVcAZNU8zHSfZd2qeQ1JDWQCk5vogcEeN459a49iSGs4CIDVUnGR/AM6pafgbgf+uaWxJLWABkJrtfdSzRfD74yRbU8O4klrCAiA1WJxkPwEur2Hoz9cwpqQWsQBIzXduxeNdHSfZjRWPKallLABS853X8PEktZAFQGq+i4A/VThe1XcUJLWQBUBquO7Det+oaLg7gP9X0ViSWswCILXD+RWN853uJkOSRpwFQGqHqo7q/WFF42hIlSW/6OPyfq7VgFkApHbIgZUVjLO8gjE0xBbM9l42o5JlVWZRvSwAUgt0nwO4ooKhLADatGKby4HVvVxajlV2p0oDYAGQ2qPfxftXcZL9qpIkGlq7nfStlRF8qIdLfx0viv+r8kCqjQVAao9+C4A//WtOtljJm4GfzOeaKIrSXV5/0R9qiqQaWACk9pgOfL1GxANPmr4jiqJ/BH49h28vgXfvfvyyL9ccSxWzAEjt8SM6p/j16n+rCqLht/vxyy4pZhckURR9dqPfVHJjWZZPHJ+cfssAo6kiUVnWcdCYpDoUefpW4OQeLl0RJ9mSqvNoNMxMTexPGS2Fcglj7FCW0WVRGa3YauGqi+//psv/HDqfemMBkFqkyNNd6Hw2u3iel74iTrKza4gkqaUsAFLLFHn6HOBzwII5XnJOnGQvqzGSKjYzNbEAWFTxsGvGJ6fXVDxmT2amJiLmX2I3pxyfnHaXy3mwAEgtVOTpS4H/BLbYzLd+GnhRnGRr60+lfsxMTfwD8GTgYGA/YGHFU8wC19B5G+RC4OPjk9MDWwBmpiYeAbyYzq/vIGDbGqb5JbCCzgOvZ45PTv++hjmGhgVAaqkiTx8EnEDnD9Wt1vlHa4HvACfGSfb9ENk0dzNTEw8CzgaeOuCpvwu8dHxy+vo6J5mZmlgI/Avwr1R/V2NTfguk45PTXxzgnK1iAZBarsjTCHgo8DDgN8CPPfCnHWamJh4CXArsGCjCn4HDxyenq9hl8l66t/rPo3NnI5Q3jU9Onxpw/sayAEhSIDNTE18Hnhg4xqXAoeOT0z1t/7spM1MTrwHOqHrceVoFLBmfnL4ycI7GcR8ASQpgZmriZYRf/KHzefybqh50ZmpiV+DdVY/bg8XAOaFDNJEFQJLCODJ0gHU8u4Yxn8j6z6aEtHRmauLBoUM0jQVAksJYGjrAOg7oPqxXpYMrHq9fTfr9bgQLgCQN2MzUxAOA+4fOsY4tgD0rHvOAisfr14GhAzSNBUCSBu9mYGXoEOso6bxDX6VfVDxev24KHaBpLACSNGDdJ+4vC51jHTPjk9O3VjzmiorH69ey0AGaxgIgSWE0aZOmi1syZq9uBXwN8B4sAJIUxrvobNwU2u3AW6sedHxy+vvA56set0dvaso5CE1iAZCkAMYnp28GjgmdAzhufHL6hprGfiXwu5rGnqvzxyenPQlzAywAkhRId5/6Y+hsyTtoq4C3AFldE4xPTv+OzhkHV9c1x2Z8EXhhoLkbz62AJSmwmamJceCDwGOBuObpVgMXAa8e1Pa4M1MTi4GTgaMYzLkHNwAnjk9Of3IAc7WWBUCSGmJmamIRkNB5h37LiodfBeTAFeOT08EOi5qZmtgNWALsXPHQJTADrOh+vKLNsABIkjSCqt76UZI0hJafNbFo+z+UB4yNje24au3Yin3e8kN/ym457wBIkjbq+vdMPG6M6J1lWR5M52Q9ACKYmS3Lz6xaterk/U7Ki4AR1SMLgCTpXm46/fAtVxfFVAmvAaJNfOuPxsbGXrTbcZc0aWdDzYGvAUqS7mV1UXyohNey6cUfYP/Z2dkLf/6egx80iFyqjgVAkrSen0wtfVYJL5rHJTusYcFHagukWlgAJEnriSj/c77XlGV5xE/fs/SZdeRRPSwAkqS7/eSUiT0i6Ol2/mxZPrrqPKqPBUCSdLdoNlra88Vl2fu1GjgLgCTpbmOUD+/12iiKer5Wg2cBkCTdrYxY1Mfl/VyrAbMASJI0giwAkiSNIAuAJEkjyAIgSdIIsgBIkjSCLACSJI0gC4AkSSPIAiBJ0giyAEiSNIIsAJIkjSALgCRJI8gCIEnSCLIASJI0giwAkiSNIAuAJEkjyAIgSdIIsgBIkjSCLACSJI0gC4AkSSPIAiBJultEdFsfl/dzrQbMAiBJutvs7OzyXq+NoOdrNXgWAEnS3VaXC5f1fHEU9X6tBs4CIEm62z5v+eHNlHy3h0vXMDb7v5UHUm0sAJKk9S1Y+3LgzvlcUpbl1O5vWn5FTYlUAwuAJGk948ddel1Eedw8LlmxatWqk2sLpFpYACRJ97L75PIzmY2eDvxqE99WRiXvj+P4r/Y7KS8GlU3ViMqyDJ1BktRQN51++I6rVhevjspoaUm5JILtoyi6vCxZEY3Nfnb345b38ryAGsACIEmahygCF45h4EcAkqR5cPEfFhYASZJGkAVAkqQRZAGQJGkEWQAkSRpBFgBJkkaQBUCSpBFkAZAkaQRZACRJGkH/H5qpXLTiWmojAAAAAElFTkSuQmCC"
card_back = "https://imgur.com/vm6MQ0e.png"
cards = []
no_of_cards = {}
card_image = {}
card_image_back = {}
card_text = {}
card_id = {}
deck_ids = ['"DeckIDs":[']
card_objects = []
custom_deck = ['"CustomDeck":{']
transform = '"Transform":{"posX":0,"posY":0,"posZ":0,"rotX":0,"rotY":180,"rotZ":180,"scaleX":1,"scaleY":1,"scaleZ":1}'
object_save_dir = os.path.expanduser('~\Documents\My Games\Tabletop Simulator\Saves\Saved Objects\\')

def now_date():
    return str(time.strftime("%m/%d/%Y"))


def user_prompt_window(message, title):
    pframe = wx.Frame(None, -1, 'win.py')
    pframe.SetSize(0, 0, 200, 50)
    try:
        dlg = wx.TextEntryDialog(pframe, message, title)
        if dlg.ShowModal() == wx.ID_OK:
            if dlg.GetValue() == '':
                wx.MessageBox('You Must Populate The Text Box To Proceed.', 'Invalid Entry',
                              wx.OK | wx.ICON_EXCLAMATION)
                return
            else:
                return dlg.GetValue()
        else:
            return False
    finally:
        dlg.Destroy()


def prompt_user_for(message, title):
    var = user_prompt_window(message, title)
    while var is None:
        var = user_prompt_window(message, title)
    if not var:
        return False
    else:
        update_status_bar(main_window, 'Input Accepted')
        return var


def user_cancelled_action():
    update_status_bar(main_window, 'User Cancelled')
    time.sleep(0.5)
    update_status_bar(main_window, '')


def update_status_bar(window, text):
    set_status = str(text)
    print(set_status)
    window.statusbar.SetStatusText(set_status)
    window.Refresh()
    window.Update()
    wx.SafeYield(win=None, onlyIfNeeded=False)


def warning(e):
    print('Warning:\n' + e)
    wx.MessageBox(e, 'Warning', wx.OK | wx.ICON_WARNING)


def information(i):
    print('Note:\n' + i)
    wx.MessageBox(i, 'Note', wx.OK | wx.ICON_INFORMATION)


def resize_img(img):
    img = Image.open(img, 'r')
    size = (312, 445)
    out = img.resize(size)
    out.save('resize-output.png')
    return Image.open('resize-output.png')


def add_card_to_deck(card, offset, deck_img, deck_name):
    img = Image.open(card)
    deck_img.paste(img, offset)
    deck_img.save(deck_name)
    deck_img = Image.open(deck_name)


def create_object(card_name):
    card = card_name
    text = card_text[card_name]
    amount = no_of_cards[card_name]
    image_url = card_image[card_name]
    back_url = card_image_back[card_name]
    cid = int(card_id[card] * 100)
    count = 1
    while count <= int(amount):
        object_string = ('{"CardID":' + str(cid) + ',\n"Name":"Card",\n"Nickname":"' + card + '",\n' + transform + '},\n')
        card_objects.append(object_string)
        deck_ids.append(str(cid) + ',')
        count += 1
    custom_deck_string = ('"' + str(card_id[card]) + '":{\n"FaceURL":"' + image_url + '",\n"BackURL":"' +
                          back_url + '",\n"NumHeight":1,\n"NumWidth":1,\n"BackIsHidden":true},\n')
    custom_deck.append(custom_deck_string)


#       Build GUI
class MainWindow(wx.Frame):

    def __init__(self, parent, title):
        window_height = 125
        window_width = 600
        wx.Frame.__init__(self, parent, style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER,
                          title='MTG TTS Deck Builder', size=(window_width, window_height))
        #           Global Window Ref
        global main_window
        main_window = self
        panel = wx.Panel(self)
        self.currentDirectory = os.getcwd()
        self.text_list_dir = wx.TextCtrl(panel, pos=(5, 5), size=(window_width - 125, 25))
        #           Set Icon
        seperator = PyEmbeddedImage(ico_img)
        icon = seperator.GetIcon()
        self.SetIcon(icon)
        #           Create Status Bar
        self.statusbar = self.CreateStatusBar(1)
        self.statusbar.SetStatusText('')
        #           Create Button(S)
        import_btn = wx.Button(panel, label='Browse', pos=(window_width - 100, 7))
        parse_file = wx.Button(panel, label='Import Deck', pos=(5, 35))
        #           Button Trigger
        import_btn.Bind(wx.EVT_BUTTON, self.browse_txt)
        parse_file.Bind(wx.EVT_BUTTON, self.parse_list)
        self.Bind(wx.EVT_CLOSE, self.close_window)
        self.Show(True)

    def open_dialog(self, wildcard):
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.currentDirectory,
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            for path in paths:
                path
        return path

    def browse_txt(self, event):
        try:
            path = self.open_dialog('*.txt')
            self.text_list_dir.SetValue(path)
        except UnboundLocalError as e:
            return

    def parse_list(self, event):
        deck_list = str(self.text_list_dir.GetValue())
        card_number = 1
        if deck_list.endswith('.txt'):
            print(deck_list)
            deck_file_name = deck_list[:-3]
            deck_name = os.path.basename(deck_list)[:-4]
            card_objects.append('{\n"ObjectStates":[\n{"Name":"DeckCustom",\n"ContainedObjects":[\n\n')
            lines = open(deck_list).readlines()
            for item in lines:
                if item != '\n':
                    no_of_cards[item[2:-1]] = int(item[:2])
                    cards.append(item[2:-1])
            for i in cards:
                time.sleep(.5)
                update_status_bar(self, 'Grabbing card data for:"' + i + '"')
                card = scrython.cards.Named(fuzzy=i)
                card_id[i] = card_number
                try:
                    url = card.image_uris(index=0, image_type='png')[:-11]
                    card_image[i] = url
                except TypeError as e:
                    warning('The card "' + i + '" does not exist on https://scryfall.com/ \n'
                                               'therefore this card cannot be imported')
                try:
                    text = card.oracle_text()
                    card_text[i] = text
                except KeyError as e:
                    card_text[i] = ''
                try:
                    back_of_card = card.card_faces()
                    back_url = card.image_uris(index=1, image_type='png')[:-11]
                    if back_url != url:
                        card_back_image = back_url
                    else:
                        card_back_image = card_back
                except AttributeError as e:
                    print(str(e))
                    card_back_image = card_back
                except KeyError as e:
                    print(str(e))
                    card_back_image = card_back
                card_image_back[i] = card_back_image
                card_number += 1
                create_object(i)
                time.sleep(.5)
            end_of_deck = deck_ids[-1][:-1] + '],'
            card_objects[-1] = card_objects[-1][:-1] + '],'
            deck_ids[-1] = end_of_deck
            end_of_custom_deck = custom_deck[-1][:-2]
            custom_deck[-1] = end_of_custom_deck + '},\n"Transform":{"posX":0,"posY":1,"posZ":0,"rotX":0,"rotY":180,' \
                                                    '"rotZ":180,"scaleX":1,"scaleY":1,"scaleZ":1}}]}'
            file = open(deck_file_name + 'json', 'w+')
            for x in card_objects:
                file.write(x)
            object_deck_ids = ''
            for ids in deck_ids:
                object_deck_ids += ids
            object_deck_ids += '\n'
            file.write(object_deck_ids)
            for deck in custom_deck:
                file.write(deck)
            file.close()
            shutil.copy(deck_file_name + 'json', object_save_dir)
            card_back_url = card_back_image
            response = requests.get(card_back_url)
            with open(object_save_dir + deck_name + '.png', 'wb') as card_back_download:
                card_back_download.write(response.content)
            update_status_bar(self, 'Deck Created')
            information(deck_name + " has been created.\n"
                                    "In game you can click Objects at the top of the screen, then choose Saved Objects,"
                                    "\n"
                                    "and then click your deck.")
            update_status_bar(self, 'Deck Created')
            time.sleep(1)
            update_status_bar(self, '')

    def close_window(self, event):
        update_status_bar(main_window, '-----Closing Application-----')
        frame.Destroy()
        sys.exit()


app = wx.App(False)
frame = MainWindow(None, "Window")
app.MainLoop()
wx.CallAfter(frame.Destroy)
