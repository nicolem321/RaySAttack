import torchvision.transforms as T
import matplotlib.pyplot as plt
import numpy as np
def generateImage(Dataloader, numImage, name, numPerClass):
    totalImageNum = 0
    # This method generates the images and plot them from dataloaders
    for i, (data, label) in enumerate(Dataloader):
        if i == numImage:
            break
        transform = T.Compose([
            T.ToPILImage(),
            T.Resize(32),
            T.ToTensor(),])
        for j in range(0, numPerClass):
            if (totalImageNum == numImage):
                break
            img = data[j]
            resized_img = transform(img)
            plt.imshow(np.transpose(resized_img))
            if (name == "clean"):
                print("saving clean images")
                plt.savefig("cleanImage_" + str(totalImageNum) + ".png") # save the figure to a file
            elif (name == "adv"):
                print("saving adv images")
                plt.savefig("advImage_" + str(totalImageNum) + ".png") # save the figure to a file
            plt.show()
            print("This is the", totalImageNum, "th image")
            totalImageNum += 1
        
