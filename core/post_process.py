import codecs


def del_repeat(prediction):
    out_file = codecs.open('out_file.txt', 'w', 'utf-8')
    with codecs.open(prediction, 'r', 'utf-8') as f:
        while True:
            pline = f.readline()

            if pline == '':
                break
            pline = pline.strip()

            if pline == '':
                break
            pphrase = pline[:-1].split('，')
            ophrase = []
            for p in pphrase:
                if p in ophrase:
                    continue
                else:
                    ophrase.append(p)
                # print(ophrase)
            # break
            out_file.write("，".join(ophrase) + '。\n')


if __name__ == '__main__':
    pred_file = 'best_bleu_prediction.txt'
    del_repeat(pred_file)
