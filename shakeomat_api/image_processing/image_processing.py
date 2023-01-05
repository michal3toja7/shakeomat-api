import cv2
import numpy as np
from django.db.models.fields.files import FieldFile

from shakeomat_api.image_processing.samples import get_samples_paths


class ImageProcessing:
    image = None
    cv_image = None

    def __init__(self, image: FieldFile):
        self.image = image
        self.cv_image = cv2.imread(image.path)

    def image_process(self):
        """The method searches for designated objects in the image. Based on
        this, it trims the sent image - so as to cut out unnecessary elements
        from the dump. The image object is stored in the instance."""

        for sample in get_samples_paths():
            template = cv2.imread(sample.path)
            height, width, channels = self.cv_image.shape
            template = self.image_resize(template, width)
            res = cv2.matchTemplate(
                self.cv_image, template, cv2.TM_CCOEFF_NORMED
            )
            threshold = 0.8
            loc = np.where(res >= threshold)
            cut_place = 0
            for pt in zip(*loc[::-1]):
                cut_place = sample.cut_place(
                    zip(*loc[::-1]), key=lambda item: item[1]
                )[1]
                continue
            if not cut_place:
                continue
            elif cut_place > height / 2:
                self.cv_image = self.cv_image[0:cut_place, 0:width]
                continue
            self.cv_image = self.cv_image[cut_place:height, 0:width]

    def save(self):
        """
        The method saves the changes made to the image to a file on the disk.
        """
        cv2.imwrite(self.image.path, self.cv_image)

    def image_resize(
        self, image, width=None, height=None, inter=cv2.INTER_AREA
    ):
        """
        The method resizes the image - so that the searched image is scaled to
        the base image.
        :param image: CV2 Image to resize
        :param width: The width of the image we want to achieve
        :param height: The height of the image we want to achieve
        :param inter:
        :return: Rescaled CV2 image
        """
        dim = None
        (h, w) = image.shape[:2]

        if width is None and height is None:
            return image

        if width is None:
            r = height / float(h)
            dim = (int(w * r), height)

        else:
            r = width / float(w)
            dim = (width, int(h * r))

        resized = cv2.resize(image, dim, interpolation=inter)
        return resized
