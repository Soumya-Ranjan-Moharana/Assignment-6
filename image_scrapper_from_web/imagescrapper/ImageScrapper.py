from bs4 import BeautifulSoup as bs
import os
import json
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import urlretrieve

class ImageScrapper:
    def delete_existing_image(self, list_of_images):
        for self.image in list_of_images:
            try:
                os.remove("./static/"+ self.image)
            except Exception as e:
                print('Error in deleting :: ',e)
        return 0

    def list_only_jpg_files(self, folder_name):
        self.list_of_jpg_files = []
        self.list_of_files = os.listdir(folder_name)
        print('list of files == ')
        print(self.list_of_files)
        for self.file in self.list_of_files:
            self.name_array = self.file.split('.')
            if (self.name_array[1] == 'jpg'):
                self.list_of_jpg_files.append(self.file)
            else:
                print('Filename does not end with jpg extension')
        return self.list_of_jpg_files

    def createURL(keyWord):
        keyWord = keyWord.split()
        keyWord = '+'.join(keyWord)
        url = "https://www.google.co.in/search?q=" + keyWord + "&source=lnms&tbm=isch"
        return url 

    def get_RawHtml(url, header):
        req = urllib.request.Request(url, headers=header)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        html = bs(respData, 'html.parser')
        return html

    # contains the link for Large original images, type of  image
    def getimageUrlList(rawHtml):
        imageUrlList = []
        for a in rawHtml.find_all("div", {"class": "rg_meta"}):
            link, imageExtension = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
            imageUrlList.append((link, imageExtension))

        print("There are total of ", len(imageUrlList), "images")
        return imageUrlList

    def downloadImagesFromURL(imageUrlList,image_name, header):
        masterListOfImages = []
        count=0
        ###print images
        imageFiles = []
        imageTypes = []
        
        image_counter=0
        for i, (img, Type) in enumerate(imageUrlList):
            try:
                if (count > 10):
                    break
                else:
                    count = count + 1
                req = urllib.request.Request(img, headers=header)
                try:
                    urllib.request.urlretrieve(img,"./static/"+image_name+str(image_counter)+".jpg")
                    image_counter=image_counter+1
                except Exception as e:
                    print("Image write failed:  ",e)
                    image_counter = image_counter + 1
                respData = urllib.request.urlopen(req)
                raw_img = respData.read()
                # soup = bs(respData, 'html.parser')

                imageFiles.append(raw_img)
                imageTypes.append(Type)

            except Exception as e:
                print("could not load : " + img)
                print(e)
                count = count + 1
        masterListOfImages.append(imageFiles)
        masterListOfImages.append(imageTypes)

        return masterListOfImages