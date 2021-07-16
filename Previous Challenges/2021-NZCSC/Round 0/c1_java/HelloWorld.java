import org.jasypt.encryption.StringEncryptor;
import org.jasypt.encryption.pbe.PooledPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.SimpleStringPBEConfig;

public class HelloWorld {
    public static void main(String[] args) {
        final SimpleStringPBEConfig pbeConfig = new SimpleStringPBEConfig();
        //can be picked via the environment variablee
        //TODO - hardcoding to be removed
        pbeConfig.setPassword("javacodegeek");  //encryptor private key
        pbeConfig.setAlgorithm("PBEWithMD5AndDES");
        pbeConfig.setKeyObtentionIterations("1000");
        pbeConfig.setPoolSize("1");
        pbeConfig.setProviderName("SunJCE");
        pbeConfig.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        pbeConfig.setStringOutputType("base64");

        final PooledPBEStringEncryptor pbeStringEncryptor = new PooledPBEStringEncryptor();
        pbeStringEncryptor.setConfig(pbeConfig);

        System.out.println("Hello, World");
    }
}