import reader
import helpers
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text


# df = reader.ReadData()

# # Text pre processing
# df[reader.title] = df[reader.title].apply(helpers.clean_text)
# df[reader.description] = df[reader.Description].apply(helpers.clean_text)
# df[reader.tags] = df[reader.tags].apply(helpers.clean_text)

saved_model_path = "smart_assignments_bert"

reloaded_model = tf.saved_model.load(saved_model_path)

def ReturnProbability(title):
    input = [title] 
    res = reloaded_model(tf.constant(input))
    
    
    return map_probabilty_to_dict(res.numpy())



def map_probabilty_to_dict(res):
    val = {}
    for i in range(reader.num_labels):
        val[reader.index_names[i]] = res[0][i]*100
    return val

print(ReturnProbability("replication requests"))