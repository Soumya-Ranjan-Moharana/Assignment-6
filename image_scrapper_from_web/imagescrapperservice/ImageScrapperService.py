from imagescrapper.ImageScrapper import ImageScrapper
from imagescrapperutils.ImageScrapperUtils import ImageScrapperUtils

class ImageScrapperService:
    utils = ImageScrapperUtils
    imgScrapper = ImageScrapper
    keyWord = ""
    fileLoc = ""
    image_name = ""
    header = ""

    def downloadImages( keyWord, header):
        imgScrapper = ImageScrapper
        url = imgScrapper.createURL(keyWord)
        rawHtml = imgScrapper.get_RawHtml(url, header)
        
        imageURLList = imgScrapper.getimageUrlList(rawHtml)
        
        masterListOfImages = imgScrapper.downloadImagesFromURL(imageURLList,keyWord, header)
        
        return masterListOfImages

    def get_image_urls(keyWord, header):
        imgScrapper = ImageScrapper
        url = imgScrapper.createURL(keyWord)
        rawHtml = imgScrapper.get_RawHtml(url, header)

        imageURLList = imgScrapper.getimageUrlList(rawHtml)

        return imageURLList
