
import argparse
import errno
import glob
import os

import cv2

from multiprocessing.pool import ThreadPool


IMG_EXTS = ["png", "jpeg", "jpg", "gif", "tiff", "tif", "raw", "bmp"]


def main(args):
    files = [x for x in glob.glob(os.path.join(args.input, "*"))
             if os.path.splitext(x)[-1].replace(".", "").lower() in IMG_EXTS]
    if not files:
        raise RuntimeError(
            "No image files in input folder {}"
            .format(args.input))

    try:
        not_empty = not all([os.path.isdir(x) for x in
                             glob.glob(os.path.join(args.output, "*"))])
        if not_empty:
            raise RuntimeError("Output directory is not empty - aborting.")
        os.makedirs(args.output)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    def resize(path):
        img = cv2.imread(path, cv2.CV_LOAD_IMAGE_COLOR)
        if img is None:
            return

        dims = img.shape[:2]
        if args.action == "scale":
            dsize = tuple([int(args.scale * x) for x in dims])[::-1]
        elif args.action == "shape":
            dsize = tuple(map(int, args.shape))
        elif args.action == "limit":
            max_dim = max(dims)
            scale = float(args.limit) / max_dim
            dsize = tuple([int(scale * x) for x in dims])[::-1]

        _img = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)
        _, img_name = os.path.split(path)
        outpath = os.path.join(args.output, img_name)
        cv2.imwrite(outpath, _img)
        return "{} -> {}".format(path, outpath)

    pool = ThreadPool(args.processes)
    for res in pool.imap_unordered(resize, files):
        print res
    pool.close()
    pool.join()


if __name__ == '__main__':
    """Batch resize image files in a folder using cv2.resize

    usage: batchScale.py [-h] [-p PROCESSES] input output {scale,shape,limit} ...

    Batch resize image files in a folder using cv2.resize

    positional arguments:
      input                 Input directory to search for image files
      output                Output folder to place image files
      {scale,shape,limit}   Action

    Notes:
    ------
    - Works on file types accepted by openCV: png, jpeg, jpg, gif, tiff,
      tif, raw, bmp

    - Treats all images as color (i.e., 3 channels)

    - The output folder must be empty or an error is raised

    Examples:
    ---------

    Scale by a constant factor (e.g., reduce to 50%):

        $ python batchScale.py data/sample/images/ data/ scale 0.5

    Scale to a fixed shape:

        $ python batchScale.py data/sample/images/ data/ shape 320 240

    Scale to a limited maximum dimension:

        $ python batchScale.py data/sample/images/ data/ limit 320

    """
    parser = argparse.ArgumentParser(
        description="Batch resize image files in a folder using cv2.resize")
    parser.add_argument(
        "input",
        help="Input directory to search for image files")
    parser.add_argument(
        "output",
        help="Output folder to place image files")
    parser.add_argument(
        "-p", "--processes", type=int, default=2,
        help="Number of processes to use for resizing")

    subparsers = parser.add_subparsers(
        dest="action", help="Action")

    scale_parser = subparsers.add_parser("scale")
    scale_parser.add_argument(
        "scale", type=float,
        help="Multiplicative scale factor applied to both x and y dimensions")

    scale_parser = subparsers.add_parser("shape")
    scale_parser.add_argument(
        "shape", nargs=2,
        help="Output shape in num_rows, num_cols order")

    scale_parser = subparsers.add_parser("limit")
    scale_parser.add_argument(
        "limit", type=int,
        help="Size limit for the largest dimension of each image")

    args = parser.parse_args()
    main(args)
