import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import itemfreq


photos = [
  {
      "name": "01ec0fc2-8d07-4b8f-9d21-1070fa134dac.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 435
  },
  {
      "name": "07c3535b-7802-4e70-8863-c04dbc1eadd8.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "2cb3d5d5-3650-4967-8779-feb2a5b816d3.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "76c15a1d-de9d-41ff-a144-998fec7c303f.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "7f3546e8-979d-4242-97b6-67aa8543c0c8.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 853
  },
  {
      "name": "91c9ad26-c2f6-45b8-af49-f0ac47944a5e.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 697
  },
  {
      "name": "9a681f50-57fe-4052-94e2-cbc92def6fff.jpg",
      "project": "font-in-the-environment",
      "width": 551,
      "height": 689
  },
  {
      "name": "9bd2eca8-14cc-4789-81bc-c4b82891b0f2.jpg",
      "project": "font-in-the-environment",
      "width": 604,
      "height": 947
  },
  {
      "name": "9c133fdc-b7d4-41ae-95b7-a98e6b0a4005.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 854
  },
  {
      "name": "IMG_20190909_181208.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 371
  },
  {
      "name": "IMG_2661.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 853
  },
  {
      "name": "IMG_2960.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 575
  },
  {
      "name": "IMG_3206.png",
      "project": "font-in-the-environment",
      "width": 628,
      "height": 750
  },
  {
      "name": "IMG_3215.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 842
  },
  {
      "name": "IMG_3223.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 853
  },
  {
      "name": "IMG_3227.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 836
  },
  {
      "name": "IMG_3230.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 853
  },
  {
      "name": "IMG_3241.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_3244.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_3246.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_3249.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_3251.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_3255.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_3261.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_3262.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_3268.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_3300.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 880
  },
  {
      "name": "IMG_3950.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 853
  },
  {
      "name": "IMG_3959.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_3978.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 507
  },
  {
      "name": "IMG_4005.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4035.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 634
  },
  {
      "name": "IMG_4049.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 129
  },
  {
      "name": "IMG_4067.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 217
  },
  {
      "name": "IMG_4083.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 859
  },
  {
      "name": "IMG_4096.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 786
  },
  {
      "name": "IMG_4098.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 853
  },
  {
      "name": "IMG_4103.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 1611
  },
  {
      "name": "IMG_4109.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 888
  },
  {
      "name": "IMG_4121.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 429
  },
  {
      "name": "IMG_4145.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 565
  },
  {
      "name": "IMG_4200.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 484
  },
  {
      "name": "IMG_4220.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 917
  },
  {
      "name": "IMG_4230.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 1373
  },
  {
      "name": "IMG_4262.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 523
  },
  {
      "name": "IMG_4294.jpeg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 878
  },
  {
      "name": "IMG_4315.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 853
  },
  {
      "name": "IMG_4330.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 853
  },
  {
      "name": "IMG_4356.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 853
  },
  {
      "name": "IMG_4357.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 238
  },
  {
      "name": "IMG_4364.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4365.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4651.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 1396
  },
  {
      "name": "IMG_4652.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4654.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 853
  },
  {
      "name": "IMG_4655.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 875
  },
  {
      "name": "IMG_4721.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 694
  },
  {
      "name": "IMG_4722.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 1158
  },
  {
      "name": "IMG_4732.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 492
  },
  {
      "name": "IMG_4738.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4740.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 680
  },
  {
      "name": "IMG_4743.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 953
  },
  {
      "name": "IMG_4745.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4750.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 1166
  },
  {
      "name": "IMG_4753.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4757.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 958
  },
  {
      "name": "IMG_4760.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 612
  },
  {
      "name": "IMG_4769.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 853
  },
  {
      "name": "IMG_4772.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 479
  },
  {
      "name": "IMG_4774.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 770
  },
  {
      "name": "IMG_4776.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 313
  },
  {
      "name": "IMG_4780.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 853
  },
  {
      "name": "IMG_4784.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 952
  },
  {
      "name": "IMG_4787.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 429
  },
  {
      "name": "IMG_4794.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 853
  },
  {
      "name": "IMG_4799.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 500
  },
  {
      "name": "IMG_4804.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 398
  },
  {
      "name": "IMG_4811.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 363
  },
  {
      "name": "IMG_4815.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 1050
  },
  {
      "name": "IMG_4817.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4828.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4832.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4834.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 621
  },
  {
      "name": "IMG_4843.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 821
  },
  {
      "name": "IMG_4845.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 860
  },
  {
      "name": "IMG_4849.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 523
  },
  {
      "name": "IMG_4854.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 1004
  },
  {
      "name": "IMG_4855.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 511
  },
  {
      "name": "IMG_4857.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4858.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4868.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 580
  },
  {
      "name": "IMG_4881.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 853
  },
  {
      "name": "IMG_4884.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 335
  },
  {
      "name": "IMG_4889.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 853
  },
  {
      "name": "IMG_4894.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 479
  },
  {
      "name": "IMG_4895.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 1526
  },
  {
      "name": "IMG_4897.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 317
  },
  {
      "name": "IMG_4901.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 1762
  },
  {
      "name": "IMG_4916.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 195
  },
  {
      "name": "IMG_4919.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 873
  },
  {
      "name": "IMG_4921.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 1004
  },
  {
      "name": "IMG_4923.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 865
  },
  {
      "name": "IMG_4927.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 200
  },
  {
      "name": "IMG_4928.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4932.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 1038
  },
  {
      "name": "IMG_4943.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 923
  },
  {
      "name": "IMG_4946.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4948.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 503
  },
  {
      "name": "IMG_4951.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 476
  },
  {
      "name": "IMG_4958.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 919
  },
  {
      "name": "IMG_4960.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4961.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4962.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 861
  },
  {
      "name": "IMG_4964.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 684
  },
  {
      "name": "IMG_4965.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4966.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4968.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 1018
  },
  {
      "name": "IMG_4970.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4971.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 804
  },
  {
      "name": "IMG_4972.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 824
  },
  {
      "name": "IMG_4974.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4975.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 448
  },
  {
      "name": "IMG_4977.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 518
  },
  {
      "name": "IMG_4978.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 918
  },
  {
      "name": "IMG_4980.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4983.JPG",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 480
  },
  {
      "name": "IMG_4985.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 853
  },
  {
      "name": "IMG_4987.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 949
  },
  {
      "name": "IMG_4990.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 927
  },
  {
      "name": "IMG_4994.jpg",
      "project": "font-in-the-environment",
      "width": 640,
      "height": 950
  },
  {
      "name": "12-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "13-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "14-02-01-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "16-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "17-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "20-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "22-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "29-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "30-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "32-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "34-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "35-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "36-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "38-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "39-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "40-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "41-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "42-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "43-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "48-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "50-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "51-01.png",
      "project": "image-and-typography",
      "width": 640,
      "height": 452
  },
  {
      "name": "0PotGf9gSZmLLhYuR7ttUQ_thumb_4cb5.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "0TX0XYytR8yW1i5lkpZheA_thumb_4c34.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 684
  },
  {
      "name": "2-bukvy-15.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 452
  },
  {
      "name": "2-bukvy-2.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 452
  },
  {
      "name": "2-bukvy-21.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 452
  },
  {
      "name": "2-bukvy-29.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 452
  },
  {
      "name": "2-bukvy-39.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 452
  },
  {
      "name": "2-bukvy-43.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 452
  },
  {
      "name": "2-bukvy-46.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 452
  },
  {
      "name": "2-bukvy-49.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 452
  },
  {
      "name": "2-bukvy-5.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 452
  },
  {
      "name": "2-bukvy-51.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 452
  },
  {
      "name": "2-bukvy-55.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 452
  },
  {
      "name": "2-bukvy-57.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 452
  },
  {
      "name": "2-bukvy-58.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 452
  },
  {
      "name": "2etH7E7bSGCrAtrsWRLoKw_thumb_5013.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 480
  },
  {
      "name": "4Mu90UpWQZihwNjkFN6dDw_thumb_4b6c.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "7m88nZLlTZ2bYDrI+VOK8w_thumb_4f05.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "9Rr05EJDTTWNqL4oFzDzhw_thumb_5058.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "a1iO114jTSiEi8aZUXcEvg_thumb_4f33.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "a2wKXHmtR7SFOvFn6u50og_thumb_4fde.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "ADehqdalRr+p0zY9lyEF0g_thumb_4b94.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 797
  },
  {
      "name": "aIWRhd9HQjGXNpdn2uaWA_thumb_4e6e.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 640
  },
  {
      "name": "aQ8JTfVUTOeDHuT7QzsFTg_thumb_4e86.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 640
  },
  {
      "name": "aqRKG2PxTLu4u8PeWIFY5w_thumb_4eef.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "B1c3RlwATvmxCQPbqw0T1Q_thumb_4e5c.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "C5NzSGWDRp2SOhqM4wDtWw_thumb_4c5c.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 710
  },
  {
      "name": "Cb+Ak0wAQjmzg9w+OJYAXw_thumb_4c91.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 902
  },
  {
      "name": "CEMRk91DSoiCoO091eJyg_thumb_5024.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 480
  },
  {
      "name": "ChYJ6QURSam0cH6+DHwIcQ_thumb_4eb9.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "CijPTMEJQNGb0HtjpZqjkg_thumb_4b8f.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 532
  },
  {
      "name": "CSZiYIkQem5EcIvmRtzg_thumb_4f01.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 907
  },
  {
      "name": "CxjiBVGASXuXEigDTqC0A_thumb_4efb.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "DwBHmzN7Se61xEGx1qtBfw_thumb_4ebf.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "E8yTXXufQ6ibhZLsI6Rtw_thumb_4f83.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "ebN7Z33QSbWtHQrT3IuIg_thumb_4ef1.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "EdVRHQX+TUuf0pJgcx3uGQ_thumb_506d.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "EjjEGJLHRvmn2URCbJRAA_thumb_4e91.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "GKrMkVVWTbGvM4CzxGpeew_thumb_4ebc.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "gM1xpY6QQvmAI9+lhsibQw_thumb_5002.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 640
  },
  {
      "name": "GOfz8GzBRhKHVY0pc35lBg_thumb_4bf3.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 860
  },
  {
      "name": "HOW98T6RTUqeexwFuuTTA_thumb_4e6a.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "IJu8ySiTEKB7aTrm3WV6w_thumb_501c.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "IPUfIASVSza4Pn9h9w420Q_thumb_5045.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "iRw6xjILQoCdvYSrPgVvAg_thumb_4b0b.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 952
  },
  {
      "name": "JjEWPD4TzSQ9qli2Pylg_thumb_5056.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "jkbpX4tXRZeP7H++W4HVgg_thumb_4eac.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "K0jEvdzjQkiwhyXt0eMwFg_thumb_4ca3.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 904
  },
  {
      "name": "lsepNXQiTh2BrUplWHOxQ_thumb_501d.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 888
  },
  {
      "name": "LSw3Two3SWyBd1PvdteM1A_thumb_4e74.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 640
  },
  {
      "name": "Ltm2ZbYuQRSyq9+WFW1pvw_thumb_4b86.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "MjK0tsXERZyR218xaRB59g_thumb_506b.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "mpHukX9sSm+VXTPSxp7Faw_thumb_4b7a.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "MYt2xH70SjGebcnlClW6w_thumb_4e5e.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 640
  },
  {
      "name": "N0M6WWLvTtu1UXX5Ns4VMQ_thumb_4c6b.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 721
  },
  {
      "name": "NEddlHJ3SV6WjpjKX1zwuA_thumb_501e.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "pjj1PgFDRBuGaaab4mdbHQ_thumb_4ce7.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "QFhkoMbQQTSJQTnHVno1A_thumb_522b.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 810
  },
  {
      "name": "rZXN2FmlRluqRpZS5a3Xg_thumb_4f1c.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 775
  },
  {
      "name": "st8yl09WQ8aOcgW9asyjAw_thumb_4ce3.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 806
  },
  {
      "name": "SVpWCza0TZeobre+ycIcw_thumb_4c59.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 891
  },
  {
      "name": "SXnKISriT86zL+yKW4Pf7A_thumb_5756.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 480
  },
  {
      "name": "tw7mUYfHRwOJF9H2DfTvKQ_thumb_4c7b.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "UaS3PIAdSZWI6cqvzDOpHA_thumb_4bda.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 860
  },
  {
      "name": "Um6tT1SxSu6MMxrWMz0kRQ_thumb_4baa.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 892
  },
  {
      "name": "UNADJUSTEDNONRAW_thumb_5032.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "UNADJUSTEDNONRAW_thumb_5076.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "UNADJUSTEDNONRAW_thumb_507b.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "UNADJUSTEDNONRAW_thumb_507d.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "UNADJUSTEDNONRAW_thumb_5088.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 835
  },
  {
      "name": "upt85tR7Sxm3MJ21QtV9fg_thumb_4be4.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 807
  },
  {
      "name": "WB0hy8UeQDCqdweRDZ0hMQ_thumb_4c46.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 725
  },
  {
      "name": "wX1+9RsvQDK9okg7bGU2gA_thumb_4ecf.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "Wzdi6mloT5qK9gE8fKvdTQ_thumb_4c18.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 749
  },
  {
      "name": "Y10eoJLDTESah1DPbFxjtA_thumb_4bc1.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 808
  },
  {
      "name": "Y1Ka0u68QMyH9+LZVod9gQ_thumb_4b57.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 880
  },
  {
      "name": "YieFFtzsTNuH7Q+OiIdvmw_thumb_4e79.jpg",
      "project": "materials-research",
      "width": 556,
      "height": 1411
  },
  {
      "name": "YQZ1aKlkTY+v7ACDFxY8CA_thumb_4c25.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 480
  },
  {
      "name": "YrkyZapkQJazH6KAeXZ1+g_thumb_4bcb.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 799
  },
  {
      "name": "ZaAtJb9JSdyrM7AKL1JK5A_thumb_5017.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 903
  },
  {
      "name": "ZfcI8BvKSxKyJ6LsddGWsw_thumb_4a42.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 868
  },
  {
      "name": "ZiCwsJhaQcqjoyq9vQ0BRA_thumb_4bfe.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "zxI9zoOtRu+BR5kIaNoEAQ_thumb_4e75.jpg",
      "project": "materials-research",
      "width": 640,
      "height": 853
  },
  {
      "name": "q11.jpg",
      "project": "subject-and-font",
      "width": 640,
      "height": 1919
  },
  {
      "name": "q12.jpg",
      "project": "subject-and-font",
      "width": 640,
      "height": 1920
  },
  {
      "name": "q13(2).jpg",
      "project": "subject-and-font",
      "width": 640,
      "height": 1920
  },
  {
      "name": "q13(3).jpg",
      "project": "subject-and-font",
      "width": 640,
      "height": 1920
  },
  {
      "name": "q13.jpg",
      "project": "subject-and-font",
      "width": 640,
      "height": 1920
  },
  {
      "name": "q14.jpg",
      "project": "subject-and-font",
      "width": 640,
      "height": 1920
  },
  {
      "name": "q15.jpg",
      "project": "subject-and-font",
      "width": 640,
      "height": 1920
  },
  {
      "name": "q2.jpg",
      "project": "subject-and-font",
      "width": 640,
      "height": 1920
  },
  {
      "name": "q3.jpg",
      "project": "subject-and-font",
      "width": 640,
      "height": 1920
  },
  {
      "name": "q4(2).jpg",
      "project": "subject-and-font",
      "width": 640,
      "height": 1920
  },
  {
      "name": "q4.jpg",
      "project": "subject-and-font",
      "width": 640,
      "height": 1920
  },
  {
      "name": "q5.jpg",
      "project": "subject-and-font",
      "width": 640,
      "height": 1920
  },
  {
      "name": "q6.jpg",
      "project": "subject-and-font",
      "width": 640,
      "height": 1920
  }
]

for photo in photos:
  p = os.path.join('.', photo['project'], photo['name'])
  print(p);
  im = imread(p)
  arr = np.float32(img)
  pixels = arr.reshape((-1, 3))

  n_colors = 5
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
  flags = cv2.KMEANS_RANDOM_CENTERS
  _, labels, centroids = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)

  palette = np.uint8(centroids)
  quantized = palette[labels.flatten()]
  quantized = quantized.reshape(img.shape)

  dominant_color = palette[np.argmax(itemfreq(labels)[:, -1])]
  print(palette)
  print(dominant_color)
  break
