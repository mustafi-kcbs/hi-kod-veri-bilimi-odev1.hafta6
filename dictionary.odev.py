
#1.

dictionary={"Alp":{"fizik":"75",
                   "kimya":"100",
                   "matematik":"85"},
            "Almira":{"fizik":"80",
                      "kimya":"95",
                      "matematik":"70"},
            "Zeynep":{"fizik":"90",
                      "kimya":"95",
                      "matematik":"75"}
                                      }
isim=input("Lutfen bir isim giriniz:")
ders_adi=input("Lutfen notunu ogrenmek istediginiz dersin adini giriniz:")
print(dictionary[isim][ders_adi])
#2
dictionary={"Alp":{"fizik":"75",
                   "kimya":"100",
                   "matematik":"85"},
            "Almira":{"fizik":"80",
                      "kimya":"95",
                      "matematik":"70"},
            "Zeynep":{"fizik":"90",
                      "kimya":"95",
                      "matematik":"75"}
                                      }

dictionary["Alp"]["matematik"]=70  #deger degistirme
print(dictionary)

isim="Nisa"      #yeni deger ekleme
ders_ismi={"fizik":"75",
                   "kimya":"80",
                   "matematik":"65"}
dictionary[isim]=ders_ismi
print(dictionary)

print(dictionary["Almira"])         #ulasmak istedigi deger sorma
print(dictionary["Zeynep"]["kimya"])